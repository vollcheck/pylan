import unittest
import datetime
from datetime import date
from unittest.mock import patch

from requests_cache import CachedSession

import pylan as p
import fixtures as f

MOCKED_FILENAME = "test_plan.csv"

class M:
    def __init__(self):
        self.status_code = 200

        with open(MOCKED_FILENAME, "r") as f:
            self.text = f.read()

class MBad:
    def __init__(self):
        self.status_code = 400
        self.text = ""

class TestPylan(unittest.TestCase):
    def setUp(self):
        self.patch = patch.object(CachedSession, 'get', return_value=M())
        with self.patch:
            self.plan = p.PlanExplorer(p.URL)

    def test_normal_execution_with_no_additional_flags(self):
        # Works only if there's internet connection.
        # Should I use mocked response here?
        assert self.plan.prepare_data() == f.normal_evaluation

    def test_wrong_subject_parameter(self):
        args = p.parse_args(['-s', 'wrong-value'])
        assert not self.plan.prepare_data(args)

    def test_wrong_requested_date_parameter(self):
        args = p.parse_args(['-d', 'wrong-value'])
        assert not self.plan.prepare_data(args)

    @patch(f'{p.__name__}.datetime', wraps=date)
    def test_requested_date_parameter(self, mock_date):
        mock_date.today.return_value = date(2022, 5, 19)
        args = p.parse_args(['-d', '28/05/2022'])
        assert self.plan.prepare_data(args) == f.requested_date

    @patch(f'{p.__name__}.datetime', wraps=date)
    def test_subject_parameter(self, mock_date):
        mock_date.today.return_value = date(2022, 5, 19)
        args = p.parse_args(['-s', 'rachunko'])
        assert self.plan.prepare_data(args) == f.subject

    def test_no_internet_connection(self):
        with patch.object(CachedSession, 'get', return_value=MBad()):
            with self.assertRaises(p.NetworkException):
                plan = p.PlanExplorer(p.URL)
                plan.prepare_data()


if __name__ == '__main__':
    unittest.main()
