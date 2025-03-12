import datetime
from collections.abc import Callable
import pytest
from unittest import mock


@pytest.fixture()
def mocked_datetime_date_today() -> None:
    with (mock.patch("datetime.date.today", return_value=datetime.date(
            2022, 2, 5)) as mock_test_datetime):
        yield mock_test_datetime


def test_datetime_date_today(mocked_datetime_date_today: Callable) -> None:
    today = datetime.date.today()
    mocked_datetime_date_today.assert_called_once()
    assert today == datetime.date(2022, 2, 5)
