# Greedy - Earliest Start Time

def est(intervals):
    intervals_sorted = sorted(intervals, key=lambda x: x[0])  # sort by start time

    selected = []
    last_finish = float("-inf")

    for (s, f) in intervals_sorted:
        if s >= last_finish:
            selected.append((s, f))
            last_finish = f

    return selected
