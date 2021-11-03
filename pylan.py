from datetime import datetime, date, timedelta
from typing import List, Dict, Optional
from io import StringIO
from csv import DictReader

from requests_cache import CachedSession
from rich.console import Console
from rich.table import Table


Plan = List[Dict[str, str]]


URL = "https://wzr.ug.edu.pl/.csv/plan_st.php?f1=N22-32&f2=4&jp=cf4f962e1fd3c99dd511843f647d568fb7957663"
session = CachedSession(
    "simple_cache",
    use_cache_dir=True,  # Save files in the default user cache dir
    cache_control=True,  # Use Cache-Control headers for expiration, if available
    expire_after=timedelta(days=7),  # Otherwise expire responses after one day
    allowable_methods=[
        "GET",
        "POST",
    ],  # Cache POST requests to avoid sending the same data twice
    allowable_codes=[
        200,
        400,
    ],  # Cache 400 responses as a solemn reminder of your failures
    # ignored_parameters=["api_key"],  # Don't match this param or save it in the cache
    match_headers=True,  # Match all request headers
    stale_if_error=True,  # In case of request errors, use stale cache data if possible
)


def download(url: str) -> Optional[Plan]:
    response = session.get(url)
    if response.status_code != 200:
        return None

    reader = DictReader(StringIO(response.text))

    # since DictReader is an iterator, not iterable,
    # we need to copy it to another structure
    return [row for row in reader]


def process(plan: Plan) -> Plan:
    today = date.today()
    dates: List[str] = [d["Start Date"] for d in plan]

    processed_dates: List[date] = [
        datetime.strptime(d, "%m/%d/%Y").date() for d in dates
    ]

    deltas: List[timedelta] = [d - today for d in processed_dates]

    min_delta = min(deltas)
    min_delta_inc = min(deltas) + timedelta(days=1)

    next_weekend_dates: List[timedelta] = [
        d for d in deltas if d == min_delta or d == min_delta_inc
    ]
    next_dates = set(dates[: len(next_weekend_dates)])

    return [d for d in plan if d["Start Date"] in next_dates]


def present(plan: Plan) -> None:
    console = Console()

    for row in plan:
        row["Date"] = row["Start Date"]
        row["Lecturer"] = row["Description"][7:]
        del row["Description"]
        del row["Start Date"]
        del row["End Date"]
        del row["Location"]

    table = Table(show_header=True)  # header_style

    headers = plan[0].keys()

    for header in headers:
        table.add_column(header)

    for row in plan:
        table.add_row(*row.values())

    console.print(table)


if __name__ == "__main__":
    plan: Optional[Plan] = download(URL)
    if plan:
        processed: Plan = process(plan)
        present(processed)
    else:
        print("Plan hasn't been downloaded")
