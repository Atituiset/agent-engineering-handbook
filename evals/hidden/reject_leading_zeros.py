import pytest

from durations import DurationError, parse_duration


@pytest.mark.parametrize(
    ("text", "expected"), [("0s", 0), ("10m", 600), ("1h0m", 3600), ("100s", 100)]
)
def test_no_leading_zero(text: str, expected: int) -> None:
    assert parse_duration(text) == expected


@pytest.mark.parametrize("text", ["01h", "00s", "1h05m", "007s"])
def test_leading_zero_rejected(text: str) -> None:
    with pytest.raises(DurationError):
        parse_duration(text)
