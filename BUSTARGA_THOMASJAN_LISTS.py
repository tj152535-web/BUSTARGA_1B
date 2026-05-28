# -------------------------------------------------------------
# Program: Adventure Quest Session Analyzer
# Description: Uses Python lists to manage inventory loot 
#              and analyze numerical chest reward stats.
# -------------------------------------------------------------

print("=== Welcome to Adventure Quest Session Analyzer ===")

# 1. Building a list from scratch using list() and append()
inventory = list()

print("\nEnter the loot items you collected (type 'done' when finished):")
while True:
    loot = input("Loot item: ").strip()
    
    # Check for sentinel value to break the loop
    if loot.lower() == 'done':
        break
        
    inventory.append(loot)

print("\n--- Inventory Report ---")
# Using len() to figure out the number of elements in the list
print("Total items collected:", len(inventory))
print("Original order of collection:", inventory)

# 2. Sorting the list in-place alphabetically
inventory.sort()
print("Alphabetically sorted inventory:", inventory)

# 3. Checking for membership using the 'in' operator
rare_item = "Mystic Sword"
if rare_item in inventory:
    print(f"✨ Amazing! You found the rare [{rare_item}]! ✨")
else:
    print(f"❌ The rare [{rare_item}] was not found this session.")

# 4. Using split() and built-in math functions
print("\n--- Gold Reward Analyzer ---")
gold_input = input("Enter gold from each chest separated by spaces (e.g., 45 120 80): ")

# split() breaks the string of spaces into a list of individual numeric strings
gold_strings = gold_input.split()

# Create a clean numeric list by iterating over the split string list
gold_rewards = list()
for reward in gold_strings:
    gold_rewards.append(int(reward))

# Make sure the user actually entered values before executing mathematical operations
if len(gold_rewards) > 0:
    print("\nRewards list per chest:", gold_rewards)
    
    # Utilizing built-in function metrics
    print("Most gold found in a single chest (max):", max(gold_rewards))
    print("Least gold found in a single chest (min):", min(gold_rewards))
    print("Total gold accumulated (sum):", sum(gold_rewards))
    
    # Combining sum() and len() to compute an exact average
    average_gold = sum(gold_rewards) / len(gold_rewards)
    print("Average gold per chest:", round(average_gold, 2))
else:
    print("No gold rewards were recorded this session.")

print("\n================ Analysis Complete ================")
