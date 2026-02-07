# Imports
import math
from utils import summarize, time_algorithm
from gen_intervals import gen_intervals
from eft import eft
from est import est
from sd import sd


def greedy_experiment(D, alphas, trials):
    results = {}  # store everything here

    ns = [2**k for k in range(10, 21)]  # 2^10 to 2^20

    for alpha in alphas:
        results[alpha] = {"n": [], "EFT": [], "EST": [], "SD": []}

        for n in ns:
            eft_times = []
            est_times = []
            sd_times = []

            for _ in range(trials):
                intervals = gen_intervals(n, D, alpha)

                eft_times.append(time_algorithm(eft, intervals))
                est_times.append(time_algorithm(est, intervals))
                sd_times.append(time_algorithm(sd, intervals))

            eft_mean, eft_std = summarize(eft_times)
            est_mean, est_std = summarize(est_times)
            sd_mean, sd_std = summarize(sd_times)

            results[alpha]["n"].append(n)
            results[alpha]["EFT"].append((eft_mean, eft_std))
            results[alpha]["EST"].append((est_mean, est_std))
            results[alpha]["SD"].append((sd_mean, sd_std))

    return results