def _pre_key(pre):
    if pre is None:
        return (1,)
    parts = []
    for p in pre.split("."):
        parts.append((0, int(p), "") if p.isdigit() else (1, 0, p))
    return (0, parts)


def semver_compare(a: str, b: str) -> int:
    def key(v):
        core, _, pre = v.partition("-")
        return tuple(int(x) for x in core.split(".")), _pre_key(pre or None)
    ka, kb = key(a), key(b)
    return (ka > kb) - (ka < kb)
