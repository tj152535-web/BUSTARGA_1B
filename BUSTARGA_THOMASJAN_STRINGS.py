# =========================================================
# PROGRAM: STUDENT PROFILE FORMATTER

print("--- String Manipulation Program ---")

# 1. Read input and strip accidental trailing spaces
user_input = input("Enter your full name: ")
clean_name = user_input.strip()

# 2. Get string length using len()
name_length = len(clean_name)
print("1. Length of your name:", name_length)

# 3. Concatenation (+) and Upper Case Library Method
print("2. Upper Case format: " + clean_name.upper())

# 4. String Slicing (Extracts first 3 characters)
nickname = clean_name[0:3]
print("3. Generated Nickname (First 3 letters): " + nickname)

# 5. Looping through a string and counting specific letters
counter = 0
for letter in clean_name.lower():
    if letter == "a":
        counter = counter + 1
print("4. Number of times the letter 'a' appears:", counter)

# 6. String Comparison (Alphabetical sorting)
if clean_name.lower() < "m":
    print("5. Group Assignment: Section Alpha")
else:
    print("5. Group Assignment: Section Beta")

print("-----------------------------------")
