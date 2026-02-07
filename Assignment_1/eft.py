# Greedy - Earliest Finish Time

def eft(intervals):
    intervals_sorted = sorted(intervals, key=lambda x: x[1])  # sort by finish time

    selected = []
    last_finish = float("-inf")

    for (s, f) in intervals_sorted:
        if s >= last_finish:
            selected.append((s, f))
            last_finish = f

    return selected