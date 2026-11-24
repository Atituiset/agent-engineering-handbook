import pytest

from durations import DurationError, parse_duration


@pytest.mark.parametrize(
    ("text", "expected"),
    [("1d", 86400), ("1d2h", 93600), ("2d30m5s", 174605), ("0d", 0), ("1h30m", 5400)],
)
def test_days(text: str, expected: int) -> None:
    assert parse_duration(text) == expected


@pytest.mark.parametrize("text", ["1h1d", "1d1d", "1s1d", "d", "1D"])
def test_days_invalid(text: str) -> None:
    with pytest.raises(DurationError):
        parse_duration(text)
