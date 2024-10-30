import sys

# data about dishes
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Greedy algorithm
def greedy_algorithm(items, budget):
    # We sort the dishes according to the decreasing ratio of calories to value
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    total_calories = 0
    chosen_items = []
    for item, info in sorted_items:
        if budget >= info["cost"]:
            chosen_items.append(item)
            budget -= info["cost"]
            total_calories += info["calories"]
    return chosen_items, total_calories


# Algorithm of dynamic programming
def dynamic_programming(items, budget):
    # Initialize the table for dynamic programming
    dp = [[0] * (budget + 1) for _ in range(len(items) + 1)]
    items_list = list(items.items())
    # We fill the table with values
    for i in range(1, len(items_list) + 1):
        name, info = items_list[i - 1]
        cost = info["cost"]
        calories = info["calories"]
        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
            else:
                dp[i][b] = dp[i - 1][b]
    # We define the selected dishes
    total_calories = dp[len(items)][budget]
    chosen_items = []
    b = budget
    for i in range(len(items), 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name = items_list[i - 1][0]
            chosen_items.append(name)
            b -= items_list[i - 1][1]["cost"]
    return chosen_items, total_calories


# Main
if __name__ == '__main__':
    try:  
        # cases
        budget = 100
        greedy_result = greedy_algorithm(items, budget)
        dp_result = dynamic_programming(items, budget)
        print("Greedy Algorithm Result:", greedy_result)
        print("Dynamic Programming Result:", dp_result)
    except (ValueError) as e:
        print(f'Something went wrong, {e}')
        sys.exit(0)

