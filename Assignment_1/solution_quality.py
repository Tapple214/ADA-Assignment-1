import statistics
from gen_intervals import gen_intervals
from eft import eft
from est import est
from sd import sd
from tos import tos
from utils import summarize

def solution_quality(D, alphas, trials, n):
    """
    Runs quality comparison experiments:
    compares EFT, EST, SD vs OPT (exhaustive solution)

    Only works for small n because exhaustive is exponential.
    """

    print("\n" + "=" * 80)
    print(f"SOLUTION QUALITY EXPERIMENTS (n = {n})")
    print("=" * 80)

    for alpha in alphas:
        print("\n" + "-" * 80)
        print(f"ALPHA = {alpha}")
        print("-" * 80)

        eft_ratios = []
        est_ratios = []
        sd_ratios = []

        for t in range(trials):
            intervals = gen_intervals(n, D, alpha)

            # Run greedy algorithms
            eft_solution = eft(intervals)
            est_solution = est(intervals)
            sd_solution = sd(intervals)

            # Run optimal exhaustive algorithm
            opt_solution = tos(intervals)

            opt_size = len(opt_solution)

            # avoid division by zero (just in case)
            if opt_size == 0:
                continue

            eft_ratios.append(len(eft_solution) / opt_size)
            est_ratios.append(len(est_solution) / opt_size)
            sd_ratios.append(len(sd_solution) / opt_size)

        eft_mean, eft_std = summarize(eft_ratios)
        est_mean, est_std = summarize(est_ratios)
        sd_mean, sd_std = summarize(sd_ratios)

        print(f"\nEFT/OPT: {eft_mean:.3f} ± {eft_std:.3f}")
        print(f"EST/OPT: {est_mean:.3f} ± {est_std:.3f}")
        print(f"SD /OPT: {sd_mean:.3f} ± {sd_std:.3f}")
