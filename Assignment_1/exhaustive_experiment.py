# Imports
from utils import summarize, time_algorithm
from tos import tos
from gen_intervals import gen_intervals

def exhaustive_experiments(D, alphas, trials):
    results = {}

    ns = list(range(5, 31, 5))  # 5, 10, 15, 20, 25, 30

    for alpha in alphas:
        results[alpha] = {"n": [], "OPT": []}

        for n in ns:
            opt_times = []

            for _ in range(trials):
                intervals = gen_intervals(n, D, alpha)
                opt_times.append(time_algorithm(tos, intervals))

            opt_mean, opt_std = summarize(opt_times)

            results[alpha]["n"].append(n)
            results[alpha]["OPT"].append((opt_mean, opt_std))

            # stop when it becomes too slow
            if opt_mean > 5.0:
                break

    return results
