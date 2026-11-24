import re

def parse_duration(s: str) -> int:
    total = 0
    for n, u in re.findall(r"(\d+)([hms])", s):
        total += int(n) * (3600 if u == "h" else 60)
    return total
