# =========================================
# Student Budget Calculator
# Created by: [Your Name]
# Topic: Python Expressions
# =========================================

# This program calculates a student's
# daily and weekly budget expenses.

# Asking the user for inputs
allowance = float(input("Enter your daily allowance: "))
food = float(input("Enter your food expenses: "))
transport = float(input("Enter your transportation expenses: "))
school = float(input("Enter your school expenses: "))

# Expressions
total_expenses = food + transport + school
remaining_money = allowance - total_expenses
weekly_savings = remaining_money * 5

# Output
print("\n===== BUDGET SUMMARY =====")
print("Total Expenses:", total_expenses)
print("Remaining Money:", remaining_money)
print("Possible Weekly Savings:", weekly_savings)

# Conditional expression
status = remaining_money > 0

print("\nDo you still have savings left?")
print(status)

# End message
print("\nThank you for using the Student Budget Calculator!")