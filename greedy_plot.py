import matplotlib.pyplot as plt
import math

def plot_greedy_runtime(greedy_results):
    for alpha, data in greedy_results.items():
        ns = data["n"]

        eft_means = [x[0] for x in data["EFT"]]
        est_means = [x[0] for x in data["EST"]]
        sd_means = [x[0] for x in data["SD"]]

        plt.figure()
        plt.loglog(ns, eft_means, marker="o", label="EFT")
        plt.loglog(ns, est_means, marker="o", label="EST")
        plt.loglog(ns, sd_means, marker="o", label="SD")

        plt.title(f"Greedy Runtime vs n (log-log), alpha={alpha}")
        plt.xlabel("n")
        plt.ylabel("runtime (seconds)")
        plt.legend()
        plt.grid(True)
        plt.savefig(f"greedy_runtime_alpha_{alpha}.png")
        plt.close()


def plot_greedy_normalized(greedy_results):
    for alpha, data in greedy_results.items():
        ns = data["n"]

        eft_norm = [data["EFT"][i][0] / (ns[i] * math.log2(ns[i])) for i in range(len(ns))]
        est_norm = [data["EST"][i][0] / (ns[i] * math.log2(ns[i])) for i in range(len(ns))]
        sd_norm = [data["SD"][i][0] / (ns[i] * math.log2(ns[i])) for i in range(len(ns))]

        plt.figure()
        plt.plot(ns, eft_norm, marker="o", label="EFT")
        plt.plot(ns, est_norm, marker="o", label="EST")
        plt.plot(ns, sd_norm, marker="o", label="SD")

        plt.title(f"Greedy Normalized Runtime t(n)/(n log2 n), alpha={alpha}")
        plt.xlabel("n")
        plt.ylabel("normalized runtime")
        plt.legend()
        plt.grid(True)
        plt.savefig(f"greedy_normalized_alpha_{alpha}.png")
        plt.close()