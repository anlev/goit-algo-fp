items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True
    )

    total_cost = 0
    total_calories = 0
    chosen_items = []

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            total_cost += data["cost"]
            total_calories += data["calories"]
            chosen_items.append(name)

    return chosen_items, total_calories, total_cost


def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost = items[names[i - 1]]["cost"]
        calories = items[names[i - 1]]["calories"]

        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(
                    dp[i - 1][b],
                    dp[i - 1][b - cost] + calories
                )
            else:
                dp[i][b] = dp[i - 1][b]

    chosen_items = []
    spent_cost = 0
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            item = names[i - 1]
            chosen_items.append(item)
            b -= items[item]["cost"]
            spent_cost += items[item]["cost"]

    chosen_items.reverse()
    return chosen_items, dp[n][budget], spent_cost


# =========================
# Example
# =========================

if __name__ == "__main__":
    budget = 100

    greedy_items, greedy_calories, greedy_cost = greedy_algorithm(items, budget)
    dp_items, dp_calories, dp_cost = dynamic_programming(items, budget)

    print("Budget:", budget)

    print("\nGreedy algorithm result:")
    print("Items:", greedy_items)
    print("Total calories:", greedy_calories)
    print("Spent cost:", greedy_cost)

    print("\nDynamic programming result:")
    print("Items:", dp_items)
    print("Total calories:", dp_calories)
    print("Spent cost:", dp_cost)
