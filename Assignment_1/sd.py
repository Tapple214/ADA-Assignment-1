# Greedy - Shortest Duration

def sd(intervals):
    intervals_sorted = sorted(intervals, key=lambda x: x[1] - x[0])  # sort by duration

    selected = []
    last_finish = float("-inf")

    for (s, f) in intervals_sorted:
        if s >= last_finish:
            selected.append((s, f))
            last_finish = f

    return selected
