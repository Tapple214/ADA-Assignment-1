import matplotlib.pyplot as plt
import math

def plot_exhaustive_runtime(exhaustive_results):
    for alpha, data in exhaustive_results.items():
        ns = data["n"]
        opt_means = [x[0] for x in data["OPT"]]

        plt.figure()
        plt.plot(ns, opt_means, marker="o", label="OPT")

        plt.title(f"Exhaustive Runtime vs n, alpha={alpha}")
        plt.xlabel("n")
        plt.ylabel("runtime (seconds)")
        plt.legend()
        plt.grid(True)
        plt.savefig(f"exhaustive_runtime_alpha_{alpha}.png")
        plt.close()


def plot_exhaustive_normalized(exhaustive_results):
    for alpha, data in exhaustive_results.items():
        ns = data["n"]

        opt_norm = [
            data["OPT"][i][0] / (ns[i] * (2 ** ns[i]))
            for i in range(len(ns))
        ]

        plt.figure()
        plt.plot(ns, opt_norm, marker="o", label="OPT normalized")

        plt.title(f"Exhaustive Normalized Runtime t(n)/(n 2^n), alpha={alpha}")
        plt.xlabel("n")
        plt.ylabel("normalized runtime")
        plt.legend()
        plt.grid(True)
        plt.savefig(f"exhaustive_normalized_alpha_{alpha}.png")
        plt.close()