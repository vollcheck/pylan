from datetime import datetime, timedelta
from typing import Callable, Dict, Generator, Optional
from io import StringIO
from csv import DictReader

import requests
from requests_cache import CachedSession
from rich.console import Console
from rich.table import Table


# Constants
URL = ("https://wzr.ug.edu.pl/.csv/plan_st.php?f1=N22-32"
       "&f2=4&jp=cf4f962e1fd3c99dd511843f647d568fb7957663")


class PlanExplorer:
    Unit = Dict[str, str]
    Plan = Generator[Unit, None, None]

    def __init__(self, url: str, use_cache: bool = False):
        if use_cache:
            self.session = self._create_session()
            response = self.session.get(url)
        else:
            response = requests.get(url)

        print(type(response))
        if response.status_code != 200:
            return None

        self.data = self._process_data(response)

    def _process_data(self, response: requests.Response) -> Plan:
        reader = DictReader(StringIO(response.text))

        # TODO: make squashing real
        return map(self._process_unit, reader)

    @staticmethod
    def _process_unit(unit) -> Unit:
        # "%m/%d/%Y %H.%M"
        return {
            "sub": unit['Subject'],
            "date": unit['Start Date'],
            "time": f"{unit['Start Time']} - {unit['End Time']}",
            "loc": unit["Location"].split(",", 1)[0]
        }

    @staticmethod
    def _create_session() -> CachedSession:
        return CachedSession(
            "simple_cache",
            use_cache_dir=True,  # Save files in the default user cache dir
            cache_control=True,  # Use Cache-Control headers for expiration, if available
            expire_after=timedelta(days=3),  # Otherwise expire responses after one day
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

    def present(self, filtering: Optional[Callable] = None) -> None:
        console = Console()
        table = Table(show_header=True)  # header_style

        # filtering part
        if filtering:
            data = (u for u in self.data if filtering(u))
        else:
            data = self.data

        first = next(data)

        # Adding headers
        for header in ["Subject", "Date", "Time", "Location"]:
            table.add_column(header)

        # Adding data
        table.add_row(*first.values())
        for row in data:
            table.add_row(*row.values())

        console.print(table)


if __name__ == "__main__":
    # TOOD: add CLI handler
    plan = PlanExplorer(URL)
    plan.present(
        lambda u: u['date'].split()[0] == "03/12/2022"
    )
