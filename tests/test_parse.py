import pytest

from durations import DurationError, parse_duration


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("0s", 0),
        ("90s", 90),
        ("1m", 60),
        ("1h30m", 5400),
        ("2h5s", 7205),
        ("1h1m1s", 3661),
    ],
)
def test_parses_valid_durations(text: str, expected: int) -> None:
    assert parse_duration(text) == expected


@pytest.mark.parametrize("text", ["", "h", "10", "1x", "1m1h", "1h1h", " 1h", "1h "])
def test_rejects_invalid_durations(text: str) -> None:
    with pytest.raises(DurationError):
        parse_duration(text)
