import time

def welcome_message():
    return "Welcome to the Expense Tracker!\nYou can log your expenses, catogerise them and view a summary of your spending." 
    #print("Welcome to the Expense Tracker!")
    #print("You can log your expenses, catogerise them and view a summary of your spending.\n")

def log_expense():
    welcome = welcome_message()
    print(welcome)
    time.sleep(5)
    while True:
        try:
            amount = float(input("Enter the expense amount: "))
            if amount <= 0:
                print("Please eneter a positive number for the amount.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    categories = ['Food', 'Transport', 'Entertainment', 'Other']
    print("\nExpense Categories:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    while True:
        try:
            category_choice = int(input("\nSelect a category by number: "))
            if category_choice < 1 or category_choice > len(categories):
                print("Please select a valid category number.")
                continue
            category = categories[category_choice - 1]
            break
        except ValueError:
            print("Invalid input. Please enter a number corresponding to a category.")

    description = input("Please enter a description for the expense: ")

    return {"amount": amount, "category": category, "description": description}

#welcome = welcome_message()
#expense = log_expense()
#print(welcome)
#print(expense)

expenses = []
def add_expense_to_list(expense):
    expenses.append(expense)

def display_summary():
    if not expenses:
        print("\nNo expenses to display.")
        return
    
    total_amount = 0
    category_totals = {}
    print("\nExpense Summary:")
    print("-" * 50)

    for expense in expenses:
        total_amount += expense['amount']
        category = expense['category']
        if category in category_totals:
            category_totals[category] += expense['amount']
        else:
            category_totals[category] = expense['amount']

    print(f"Total amount spent: £{total_amount:.2f}")

    print("\nAmount spent by category:")

    print("\nAmount spent by category:")
    for category, total in category_totals.items():
        print(f"{category}: £{total:.2f}")

    print("\nList of all expenses:")
    for expense in expenses:
        print(f"-{expense['description']} | {expense['category']} | £{expense['amount']:.2f}")

def thank_you_message():
    print("\nThank you for using the Expense Tracker! Have a nice day.")

def main():
    welcome_message()

    while True:
        print("\n1. Log an expense\n2. View expense summary\n3. Exit")

        choice = input("Please select an option: ")

        if choice == '1':
            expense = log_expense()
            add_expense_to_list(expense)
            print("\nExpense logged successfully!")
        elif choice == '2':
            display_summary()
        elif choice == '3':
            thank_you_message()
            break
        else:
            print("Invalid chocie. Please enter 1, 2 or 3.")

if __name__ == "__main__":
    main()