import random

# Roll a single die with a given number of sides
def roll_die(sides):
    return random.randint(1, sides)

# Roll multiple dice and return a list of results
def roll_multiple_dice(num_dice, sides):
    results = []
    for _ in range(num_dice):
        result = roll_die(sides)
        results.append(result)
    return results

# Show statistics for a list of dice rolls
def show_statistics(results):
    print("\n--- Dice Roll Statistics ---")
    print(f"Total rolls: {len(results)}")
    print(f"Sum of all rolls: {sum(results)}")
    print(f"Average roll: {sum(results)/len(results):.2f}")
    print(f"Highest roll: {max(results)}")
    print(f"Lowest roll: {min(results)}")
    
    # Count frequency of each number
    freq = {}
    for r in results:
        if r in freq:
            freq[r] += 1
        else:
            freq[r] = 1
    print("Frequency of each result:")
    for number in sorted(freq):
        print(f"{number}: {freq[number]}")

# -----------------------------
# Main Program
# -----------------------------
print("🎲 Welcome to Dice Rolling Simulator 🎲")

sides = int(input("Enter the number of sides on the die: "))
num_dice = int(input("Enter the number of dice to roll: "))

rolls = roll_multiple_dice(num_dice, sides)

print("\nResults of each roll:", rolls)

show_statistics(rolls)
