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


if __name__ == "__main__":
    TRIALS = 1_000_000

    monte_carlo_probs = monte_carlo_dice_simulation(TRIALS)
    analytical_probs = analytical_probabilities()

    print("Sum | Monte Carlo | Analytical")
    print("-" * 30)
    for s in range(2, 13):
        print(
            f"{s:>3} | "
            f"{monte_carlo_probs[s]:.4f}      | "
            f"{analytical_probs[s]:.4f}"
        )

    plot_probabilities(monte_carlo_probs, analytical_probs)
