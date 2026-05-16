# =========================================
# Simple Calendar and Reminder System
# Created by: Your Name
# Topic: Functions in Python
# =========================================

# list to store reminders
reminders = []


# function to add reminder
def add_reminder():
    task = input("Enter your reminder: ")
    reminders.append(task)
    print("Reminder added successfully!\n")


# function to view reminders
def view_reminders():

    if len(reminders) == 0:
        print("No reminders found.\n")

    else:
        print("\nYour Reminders:")

        count = 1

        for reminder in reminders:
            print(count, "-", reminder)
            count = count + 1

        print()


# function to delete reminder
def delete_reminder():

    view_reminders()

    if len(reminders) > 0:

        number = int(input("Enter reminder number to delete: "))

        if number >= 1 and number <= len(reminders):

            reminders.pop(number - 1)
            print("Reminder deleted successfully!\n")

        else:
            print("Invalid reminder number.\n")


# function to display menu
def show_menu():

    print("===== CALENDAR / REMINDER SYSTEM =====")
    print("1. Add Reminder")
    print("2. View Reminders")
    print("3. Delete Reminder")
    print("4. Exit")


# main program loop
while True:

    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        add_reminder()

    elif choice == "2":
        view_reminders()

    elif choice == "3":
        delete_reminder()

    elif choice == "4":
        print("Program Closed.")
        break

    else:
        print("Invalid choice.\n")