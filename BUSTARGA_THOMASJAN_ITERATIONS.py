# =================================================================
# Title: RPG Backpack Weight & Loot Analyzer
# Author: [Your Name]
# Environment: Pydroid 3 (Python 3)
# Description: Implements all Chapter 5 iteration idioms using a 
#              practical, non-generic inventory tracking scenario.
# =================================================================

# Initializing loop idiom variables
total_items = 0
total_weight = 0.0
heaviest_loot = -1.0  # Baseline tracking for largest value
lightest_loot = None  # Using None to safely establish the first entry

print("==================================================")
print("       RPG BACKPACK LOOT & WEIGHT ANALYZER        ")
print("==================================================")
print("Instructions:")
print("  - Enter the weight (numeric) of each loot item.")
print("  - Type '#' at the start of a line to add a journal note.")
print("  - Type 'done' when you are finished packing.")
print("==================================================\n")

# Indefinite loop execution
while True:
    line = input("> Enter loot item or command: ")
    
    # 1. Handle empty inputs gracefully
    if len(line) == 0:
        continue
        
    # 2. The 'continue' pattern: Skip lines designated as journal notes
    if line[0] == '#':
        print("   [Journal Note Saved: Moving to next item...]")
        continue
        
    # 3. The 'break' pattern: Exit loop when user is finished
    if line == 'done':
        print("   [Closing backpack and sealing inventory...]")
        break
        
    # Convert string input to float for math operations
    weight = float(line)
    
    # 4. Idiom: Counting items
    total_items = total_items + 1
    
    # 5. Idiom: Summing values
    total_weight = total_weight + weight
    
    # 6. Idiom: Finding the largest value (Heaviest item)
    if weight > heaviest_loot:
        heaviest_loot = weight
        
    # 7. Idiom: Finding the smallest value using 'is' logical operator
    if lightest_loot is None:
        lightest_loot = weight
    elif weight < lightest_loot:
        lightest_loot = weight

# --- End of Loop / Output Generation ---

print("\n==================================================")
print("               INVENTORY SUMMARY                  ")
print("==================================================")

# Check if items were processed to prevent division-by-zero errors
if total_items > 0:
    # Idiom: Computing average after loop termination
    average_weight = total_weight / total_items
    
    print("Total Loot Items Packed :", total_items)
    print("Total Backpack Weight   :", total_weight, "kg")
    print("Average Item Weight     :", average_weight, "kg")
    print("Heaviest Item Found     :", heaviest_loot, "kg")
    print("Lightest Item Found     :", lightest_loot, "kg")
else:
    print("Your backpack is completely empty! No valid loot recorded.")

print("==================================================")
