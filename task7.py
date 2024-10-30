import random
import matplotlib.pyplot as plt
import sys

# simulation of rolling two dice
def simulate_dice_rolls(num_rolls):
    # Dictionary initialization (from 2 to 12)
    counts = {i: 0 for i in range(2, 13)}  
    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        total = roll1 + roll2
        counts[total] += 1
    # Calculation of probabilities
    probabilities = {total: count / num_rolls for total, count in counts.items()}
    return probabilities


# Main
if __name__ == '__main__':
    try:
        # Simulation parameters (100 thousand throws)
        num_rolls = 100000
        # Conducting a simulation
        monte_carlo_probabilities = simulate_dice_rolls(num_rolls)
        # Analytical probabilities
        analytical_probabilities = {
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
            12: 1 / 36
        }

        print(f"{'Case: ':<17}{'Sum: ':<23}{'Probability: ':<15}")
        print(f"------------------------------------------------------")
        for total, prob in monte_carlo_probabilities.items():
            print(f"{'Monte-Carlo':<17}{total:<23.6f}{prob:.2%}")
        print(f"------------------------------------------------------")
        for total, prob in analytical_probabilities.items():
             print(f"{'Analitics':<17}{total:<23.6f}{prob:.2%}")
        print(f"------------------------------------------------------")

        # Visualization
        sums = list(range(2, 13))
        monte_carlo_values = [monte_carlo_probabilities[total] for total in sums]
        analytical_values = [analytical_probabilities[total] for total in sums]

        plt.plot(sums, monte_carlo_values, label="Monte-Carlo", marker='o')
        plt.plot(sums, analytical_values, label="Analitics", marker='x')
        plt.xlabel("Sum")
        plt.ylabel("Probability")
        plt.title("Comparison of the probabilities of the sums when throwing two dice")
        plt.legend()
        plt.grid(True)
        plt.show()
    except (ValueError) as e:
        print(f'Something went wrong, {e}')
        sys.exit(0)
