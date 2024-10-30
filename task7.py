import random
import matplotlib.pyplot as plt
import sys

# Функція для симуляції кидання двох кубиків
def simulate_dice_rolls(num_rolls):
    counts = {i: 0 for i in range(2, 13)}  # Ініціалізація словника для підрахунку сум (від 2 до 12)

    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        total = roll1 + roll2
        counts[total] += 1

    # Обчислення ймовірностей
    probabilities = {total: count / num_rolls for total, count in counts.items()}
    return probabilities

# Параметри симуляції
num_rolls = 100000  # Наприклад, 100 тисяч кидків

# Проведення симуляції
monte_carlo_probabilities = simulate_dice_rolls(num_rolls)

# Аналітичні ймовірності
analytical_probabilities = {
    2: 1 / 36, 3: 2 / 36, 4: 3 / 36, 5: 4 / 36, 6: 5 / 36,
    7: 6 / 36, 8: 5 / 36, 9: 4 / 36, 10: 3 / 36, 11: 2 / 36, 12: 1 / 36
}

# Порівняння результатів
print("Монте-Карло ймовірності:")
for total, prob in monte_carlo_probabilities.items():
    print(f"Сума {total}: {prob:.2%}")

print("\nАналітичні ймовірності:")
for total, prob in analytical_probabilities.items():
    print(f"Сума {total}: {prob:.2%}")

# Візуалізація результатів
sums = list(range(2, 13))
monte_carlo_values = [monte_carlo_probabilities[total] for total in sums]
analytical_values = [analytical_probabilities[total] for total in sums]

plt.plot(sums, monte_carlo_values, label="Монте-Карло", marker='o')
plt.plot(sums, analytical_values, label="Аналітичні", marker='x')
plt.xlabel("Сума")
plt.ylabel("Ймовірність")
plt.title("Порівняння ймовірностей сум при киданні двох кубиків")
plt.legend()
plt.grid(True)
plt.show()


# Main
if __name__ == '__main__':
    try:
        test()
    except (ValueError) as e:
        print(f'Something went wrong, {e}')
        sys.exit(0)
