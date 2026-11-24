def merge_intervals(items):
    out = []
    for start, end in sorted(items):
        if out and start <= out[-1][1]:
            out[-1][1] = max(out[-1][1], end)
        else:
            out.append([start, end])
    return out
