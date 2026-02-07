# True optimal solution using exhaustive algorithm
# Precompute interval compatibility

def is_compatible(subset):
    subset_sorted = sorted(subset, key=lambda x: x[0])  # sort by start time
    
    for i in range(len(subset_sorted) - 1):
        (s1, f1) = subset_sorted[i]
        (s2, f2) = subset_sorted[i + 1]
        
        if f1 > s2:   # overlap condition
            return False
    
    return True

def tos(intervals):
    n = len(intervals)
    best_subset = []

    for mask in range(1 << n):  # 2^n subsets
        subset = []

        for i in range(n):
            if mask & (1 << i):  # if i-th interval is included
                subset.append(intervals[i])

        if is_compatible(subset):
            if len(subset) > len(best_subset):
                best_subset = subset

    return best_subset
