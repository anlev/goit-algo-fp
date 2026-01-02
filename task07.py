import random
from collections import defaultdict
import matplotlib.pyplot as plt


def monte_carlo_dice_simulation(num_trials):
    results = defaultdict(int)

    for _ in range(num_trials):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        results[die1 + die2] += 1

    probabilities = {
        total: count / num_trials
        for total, count in results.items()
    }

    return probabilities


def analytical_probabilities():
    return {
        2: 1 / 36,
        3: 2 / 36,
        4: 3 / 36,
        5: 4 / 36,
        6: 5 / 36,
        7: 6 / 36,
        8: 5 / 36,
        9: 4 / 36,
        10: 3 / 36,
        11: 2 / 36,
        12: 1 / 36,
    }


def plot_probabilities(monte_carlo, analytical):
    sums = range(2, 13)

    monte_values = [monte_carlo.get(s, 0) for s in sums]
    analytical_values = [analytical[s] for s in sums]

    plt.figure(figsize=(8, 5))
    plt.bar(sums, monte_values, alpha=0.7, label="Monte Carlo")
    plt.plot(sums, analytical_values, color="red", marker="o", label="Analytical")

    plt.xlabel("Sum of dice")
    plt.ylabel("Probability")
    plt.title("Monte Carlo Simulation vs Analytical Probabilities")
    plt.legend()
    plt.grid(True)

    plt.show()


def calculate_errors(monte_carlo, analytical):
    errors = {}
    total_error = 0

    for s in range(2, 13):
        error = abs(monte_carlo.get(s, 0) - analytical[s])
        errors[s] = error
        total_error += error

    mean_absolute_error = total_error / 11
    return errors, mean_absolute_error


def plot_error_convergence(trials_list, analytical):
    maes = []

    for trials in trials_list:
        monte_carlo = monte_carlo_dice_simulation(trials)
        _, mae = calculate_errors(monte_carlo, analytical)
        maes.append(mae)

    plt.figure(figsize=(8, 5))
    plt.plot(trials_list, maes, marker="o")
    plt.xscale("log")
    plt.xlabel("Number of trials (log scale)")
    plt.ylabel("Mean Absolute Error (MAE)")
    plt.title("Monte Carlo Error Convergence")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    trials_list = [100, 1_000_000]
    analytical_probs = analytical_probabilities()

    for trials in trials_list:
        monte_carlo_probs = monte_carlo_dice_simulation(trials)
        errors, mae = calculate_errors(
            monte_carlo_probs,
            analytical_probs
        )

        print(f"\nNumber of trials: {trials}")
        print("Sum | Monte Carlo | Analytical | Error")
        print("-" * 45)

        for s in range(2, 13):
            print(
                f"{s:>3} | "
                f"{monte_carlo_probs.get(s, 0):.4f}     | "
                f"{analytical_probs[s]:.4f}     | "
                f"{errors[s]:.4f}"
            )

        print(f"Mean Absolute Error (MAE): {mae:.6f}")

    # Probability comparison plot
    monte_carlo_probs = monte_carlo_dice_simulation(1_000_000)
    plot_probabilities(monte_carlo_probs, analytical_probs)

    # Error convergence plot
    convergence_trials = [100, 500, 1_000, 5_000, 10_000, 100_000, 1_000_000]
    plot_error_convergence(convergence_trials, analytical_probs)

