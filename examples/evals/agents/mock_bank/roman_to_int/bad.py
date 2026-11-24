_VAL = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_int(s: str) -> int:
    total = 0
    for i, ch in enumerate(s):
        v = _VAL[ch]
        total += -v if i + 1 < len(s) and _VAL[s[i + 1]] > v else v
    return total
