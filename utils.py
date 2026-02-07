# Imports
import statistics
import time
from gen_intervals import gen_intervals
from eft import eft
from est import est
from sd import sd
from tos import tos

# Mean and Standard Deviation Calculation
def summarize(values):
    mean_val = statistics.mean(values)
    std_val = statistics.stdev(values) if len(values) > 1 else 0.0
    return mean_val, std_val

# Timing Rules
def time_algorithm(algorithm, intervals):
    start = time.perf_counter()
    algorithm(intervals)
    end = time.perf_counter()
    return end - start

# Warm-up Function
def warm_up(D, alphas):
    intervals = gen_intervals(20, D, alphas[0])
    eft(intervals)
    est(intervals)
    sd(intervals)

    small_intervals = gen_intervals(10, D, alphas[0])
    tos(small_intervals)