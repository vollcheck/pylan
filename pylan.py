import argparse
from datetime import datetime, timedelta
from typing import Callable, Dict, Generator, Optional
from io import StringIO
from csv import DictReader

import requests
from requests_cache import CachedSession
from rich import print as rprint
from rich.console import Console
from rich.table import Table, Column


# Constants
URL = ("https://wzr.ug.edu.pl/.csv/plan_st.php?f1=N22-32"
       "&f2=4&jp=cf4f962e1fd3c99dd511843f647d568fb7957663")


def print_error(msg: str) -> None:
    rprint(f"[bold red]{msg}[/bold red]")


class PlanExplorer:
    Unit = Dict[str, str]
    Plan = Generator[Unit, None, None]

    def __init__(self, url: str, use_cache: bool = False):
        if use_cache:
            self.session = self._create_session()
            response = self.session.get(url)
        else:
            response = requests.get(url)

        if response.status_code != 200:
            message = "No connection!"
            print_error(message)
            raise Exception(message)

        self.data = self._process_data(response)
        self.data = self._squash_rows()

    @staticmethod
    def _process_unit(unit: Unit) -> Unit:
        # "%m/%d/%Y %H.%M"
        return {
            "sub": unit['Subject'],
            "date": unit['Start Date'],
            "stime": unit['Start Time'],
            "etime": unit['End Time'],
            "loc": unit["Location"].split(",", 1)[0]
        }

    def _process_data(self, response: requests.Response) -> Plan:
        reader = DictReader(StringIO(response.text))
        return [self._process_unit(u) for u in reader]

    def _squash_rows(self):
        result = []
        prev = None

        for row in self.data:
            if (
                prev
                and prev['date'] == row['date']
                and prev['sub'] == row['sub']
            ):
                last_r = result.pop() if result else row
                print("merged", last_r['sub'], last_r['etime'], row['etime'])
                last_r['etime'] = row['etime']
                result.append(last_r)

            else:
                result.append(row)

            prev = row

        return result



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
        table = Table(
            "Subject",
            "Date",
            "Start Time",
            "End Time",
            Column(header="Location", justify="center")
        )

        # TODO: filtering part
        if filtering:
            data = [u for u in self.data if filtering(u)]
        else:
            data = self.data

        # Adding data
        for row in data:
            table.add_row(*row.values())

        console.print(table)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='UG plan downloader.')
    parser.add_argument(
        '--filter-by', dest='column', type=str, help='filter by the exact column'
    )

    args = parser.parse_args()
    if not args.column:
        print_error("You passed no args!")

    print(args.column)  # for testing

    plan = PlanExplorer(URL)
    # lambda u: u['date'].split()[0] == "03/12/2022"
    plan.present()
