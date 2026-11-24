import pytest

from durations import DurationError, parse_duration


@pytest.mark.parametrize(
    ("text", "expected"),
    [("1h 30m", 5400), ("1h  30m", 5400), ("2h 5s", 7205), ("1h 1m 1s", 3661), ("90s", 90)],
)
def test_spaces_between_pairs(text: str, expected: int) -> None:
    assert parse_duration(text) == expected


@pytest.mark.parametrize("text", [" 1h", "1h ", "1h\t30m", "1h 1h", "30m 1h", "1 h", " "])
def test_spaces_invalid(text: str) -> None:
    with pytest.raises(DurationError):
        parse_duration(text)
