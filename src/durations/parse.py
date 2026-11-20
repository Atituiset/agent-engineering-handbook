"""Duration parsing.

Grammar: one or more ``<integer><unit>`` pairs, units in strictly descending
order, each unit at most once. Supported units: ``h`` (hours), ``m`` (minutes),
``s`` (seconds). Examples: ``"90s"``, ``"1h30m"``, ``"2h5s"``.
"""

import re

_UNIT_SECONDS: dict[str, int] = {"h": 3600, "m": 60, "s": 1}
_UNIT_ORDER = list(_UNIT_SECONDS)
_TOKEN = re.compile(r"(\d+)([a-z])")


class DurationError(ValueError):
    """Raised when a duration string is malformed."""


def parse_duration(text: str) -> int:
    """Return the total number of seconds in ``text``.

    Raises:
        DurationError: if ``text`` is empty, has an unknown unit, repeats a unit
            or lists units out of order.
    """
    if not text:
        raise DurationError("empty duration")
    pos = 0
    total = 0
    last_rank = -1
    for match in _TOKEN.finditer(text):
        if match.start() != pos:
            raise DurationError(f"unexpected character at {pos}: {text!r}")
        amount, unit = int(match.group(1)), match.group(2)
        if unit not in _UNIT_SECONDS:
            raise DurationError(f"unknown unit {unit!r} in {text!r}")
        rank = _UNIT_ORDER.index(unit)
        if rank <= last_rank:
            raise DurationError(f"unit {unit!r} repeated or out of order in {text!r}")
        last_rank = rank
        total += amount * _UNIT_SECONDS[unit]
        pos = match.end()
    if pos != len(text):
        raise DurationError(f"unexpected trailing input at {pos}: {text!r}")
    return total
