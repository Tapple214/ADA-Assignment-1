# Imports
import random

def gen_intervals(n,D,alpha):
    T = alpha * n * D
    intervals = []

    for _ in range(n):
        s = random.uniform(0, T)
        d = random.uniform(1, D)
        f = s + d
        intervals.append((s, f))

    return intervals