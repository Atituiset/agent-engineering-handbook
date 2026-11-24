def semver_compare(a: str, b: str) -> int:
    ka = [int(x) for x in a.split("-")[0].split(".")]
    kb = [int(x) for x in b.split("-")[0].split(".")]
    return (ka > kb) - (ka < kb)
