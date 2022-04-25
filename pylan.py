import argparse
import sys
from datetime import date, datetime, timedelta
from typing import Dict, List, Optional
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


# Types

Unit = Dict[str, str]
Plan = List[Unit]


# Helpers functions

def print_error(msg: str) -> None:
    rprint(f"[bold red]{msg}[/bold red]")


# My own exception
class NetworkException(Exception):
    pass


class PlanExplorer:
    def __init__(self, url: str, use_cache: bool = True):
        if use_cache:
            self.session = self._create_session()
            response = self.session.get(url)
        else:
            response = requests.get(url)

        if response.status_code != 200:
            message = "No connection!"
            print_error(message)
            raise NetworkException(message)

        self.data = self._process_data(response)
        self.data = self._squash_rows()

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

    def _process_unit(self, unit: Unit) -> Unit:
        return {
            "sub": unit['Subject'],
            "date": datetime.strptime(unit['Start Date'], "%m/%d/%Y").strftime("%d/%m/%Y"),
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
                last_r['etime'] = row['etime']
                result.append(last_r)

            else:
                result.append(row)

            prev = row

        return result

    @staticmethod
    def get_next_weekend(plan: Plan) -> Plan:
        today = date.today()
        dates: List[str] = [d["date"] for d in plan]

        processed_dates: List[date] = [
            datetime.strptime(d, "%d/%m/%Y").date() for d in dates
        ]

        deltas: List[timedelta] = [d - today for d in processed_dates]

        min_delta = min(deltas)  # closest weekend (Saturday)
        min_delta_inc = min(deltas) + timedelta(days=1) # closest weekend (Sunday)

        next_weekend_dates: List[timedelta] = [
            d for d in deltas if d == min_delta or d == min_delta_inc
        ]
        next_dates = set(dates[:len(next_weekend_dates)])

        return [d for d in plan if d["date"] in next_dates]

    def prepare_data(self, args: Optional[argparse.Namespace] = None) -> Optional[Plan]:
        data = self.data
        if args:
            if args.subject:
                data = [d for d in self.data if args.subject in d['sub'].lower()]

            if args.requested_date:
                # TODO: Validate date? (for now it's just string comparison)
                data = [d for d in self.data if args.requested_date == d['date'].lower()]

            if args.next:
                data = self.get_next_weekend(data)

        if not data:
            rprint(f"[bold orange]Cannot print plan with given options,"
                   " check your argument parameters.[/bold orange]")
            return

        return data


    def present(self, args: argparse.Namespace = None) -> Optional[int]:
        console = Console()
        table = Table(
            "Subject",
            "Date",
            "Start Time",
            "End Time",
            Column(header="Location", justify="center")
        )

        data = self.prepare_data(args)
        if not data:
            return

        # Adding data
        for row in data:
            table.add_row(*row.values())

        console.print(table)

def parse_args(args: list) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='UG plan downloader.')
    parser.add_argument(
        "-s", "--subject", dest='subject', type=str, help='filter by the name of subject'
    )
    parser.add_argument(
        "-d", "--date", dest='requested_date', type=str, help='show the plan for requested date'
    )
    parser.add_argument(
        "-n", "--next", action='store_true', help='show the plan for next week'
    )  # TODO: make a flag out of it

    return parser.parse_args(args)


def main():
    plan = PlanExplorer(URL)
    cli_args = sys.argv[1:] # omit the prog name
    args = parse_args(cli_args)
    plan.present(args)

if __name__ == "__main__":
    main()
