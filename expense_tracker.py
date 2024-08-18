expenses = [] # A list to store expenses


def add_expense(): # function will prompt the user to enter the details of the expense and then store this data in the expenses list. 
    name = input("Enter the name of the expense: ")
    amount = float(input("Enter the amount spent: "))
    category = input("Enter the category: ")


    # Creates a dictionary to store the expense details
    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }


    # Adds expenses to the list
    expenses.append(expense)


    print(f"expense '{name}' added successfully!\n")



def view_expenses():
    if not expenses: # Checks if the expenses list is empty
        print("No expenses recorded yet.\n")
        return
    

    print("Your Expenses:")
    total_amount = 0 # Initializes a variable to store the total amount spent


    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - ${expense['amount']:.2f} ({expense['category']})")
        total_amount += expense['amount']


    print(f"\nTotal Amount Spent: ${total_amount:.2f}\n")   


def delete_expense():
    view_expenses()


    if not expenses: # If there are no expenses, exits function
        return


    try:
        task_number = int(input("Enter the number of the expense you want to delete "))
        if 1 <= task_number <= len(expenses):
            removed_expense = expenses.pop(task_number - 1)
            print(f"Expense '{removed_expense['name']}' deleted successfully.\n")
        else:
            print("Invalid input. Please enter a valid number.\n")
    except ValueError:
            print("Invalid input. Please enter a number. \n")


def save_expenses():
    with open("expenses.txt", "w") as file: # Opens file in write mode
        for expense in expenses:
            file.write(f"{expense['name']},{expense['amount']},{expense['category']}\n")
    print("Expenses saved successfully.")


def load_expenses():
    try:
        with open("expenses.txt", "r") as file: # Opens file in read mode
            for line in file:
                name, amount, category = line.strip().split(",")
                expenses.append({"name": name, "amount": float(amount), "category": category})
        print("Expenses loaded successfully.\n")
    except FileNotFoundError:
        print("No saved expenses found. Starting with an empty list.\n")



def main():
    load_expenses() # Loads the expenses when the program starts


    while True:
        print("Personal Expenses Tracker")
        print("1. Add an Expense")
        print("2. View Expenses")
        print("3. Delete an Expense")
        print("4. Exit")


        choice = input("Enter your choice (1/2/3/4): ")


        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            save_expenses() # Saves the expenses when the program exits
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
