import re

_PART = re.compile(r"(\d+)([hms])")

def parse_duration(s: str) -> int:
    if not s or _PART.sub("", s) != "":
        raise ValueError(f"invalid duration: {s!r}")
    unit = {"h": 3600, "m": 60, "s": 1}
    return sum(int(n) * unit[u] for n, u in _PART.findall(s))
