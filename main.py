# Imports
from greedy_experiment import greedy_experiment
from exhaustive_experiment import exhaustive_experiments
from utils import warm_up
from solution_quality import solution_quality
from greedy_plot import plot_greedy_runtime, plot_greedy_normalized
from exhaustive_plot import plot_exhaustive_runtime, plot_exhaustive_normalized

# Constants
D = 50
alphas = [0.1, 1.0, 5.0]
trials = 10

# Benchmarking Main Function
def main():
    warm_up(D, alphas)
    print("Finished warmup")

    solution_quality(D, alphas, trials, n=20)
    print("Finished solution_quality")

    greedy_results = greedy_experiment(D, alphas, trials)
    print("Finished greedy_experiment")

    exhaustive_results = exhaustive_experiments(D, alphas, trials)
    print("Finished exhaustive_experiments")

    print("Now plotting...")

    # Generate plots
    plot_greedy_runtime(greedy_results)
    plot_greedy_normalized(greedy_results)

    plot_exhaustive_runtime(exhaustive_results)
    plot_exhaustive_normalized(exhaustive_results)

    print("\nAll plots saved as PNG files.")

if __name__ == "__main__":
    main()
