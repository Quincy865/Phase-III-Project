from lib.db.models import User, Transaction, SavingsGoal, session
from lib.helpers import display_table, get_user_input
from datetime import datetime

def main_menu():
    while True:
        print("\n--- Finance Tracker ---")
        print("1. Add a User")  
        print("2. Delete a User")  
        print("3. View Transactions")
        print("4. Add a Transaction")
        print("5. Update a Transaction")
        print("6. Delete a Transaction")
        print("7. View Savings Goals")
        print("8. Set a Savings Goal")
        print("9. Delete a Savings Goal")  
        print("10. Exit") 

        choice = input("Enter your choice: ")
        if choice == "1":
            add_user()
        elif choice == "2":
            delete_user()
        elif choice == "3":
            display_transactions()
        elif choice == "4":
            add_transaction()  
        elif choice == "5":
            update_transaction()
        elif choice == "6":
            delete_transaction()
        elif choice == "7":
            display_savings_goals()
        elif choice == "8":
            set_savings_goal()
        elif choice == "9":
            delete_savings_goal() 
        elif choice == "10":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def display_transactions():
    transactions = session.query(Transaction).all()
    data = [(t.id, t.description, t.amount, t.date) for t in transactions]
    display_table(data, headers=["ID", "Description", "Amount", "Date"])

def delete_transaction():
    display_transactions()
    transaction_id = get_user_input("Enter the ID of the transaction to delete: ", int)
    transaction_to_delete = session.query(Transaction).filter_by(id=transaction_id).first()

    if transaction_to_delete:
        session.delete(transaction_to_delete)
        session.commit()
        print(f"Transaction with ID {transaction_id} has been deleted.")
    else:
        print("Transaction not found.")

def update_transaction():
    display_transactions()
    transaction_id = get_user_input("Enter the ID of the transaction to update: ", int)
    transaction_to_update = session.query(Transaction).filter_by(id=transaction_id).first()

    if transaction_to_update:
        print(f"Updating transaction with ID {transaction_id}")
        new_description = get_user_input("New Description (leave empty to keep current): ")
        new_amount = get_user_input("New Amount (leave empty to keep current): ", float)
        new_date = get_user_input("New Date (leave empty to keep current): ")

        # Update only if new values are provided
        if new_description:
            transaction_to_update.description = new_description
        if new_amount:
            transaction_to_update.amount = new_amount
        if new_date:
            transaction_to_update.date = new_date

        session.commit()
        print(f"Transaction with ID {transaction_id} has been updated.")
    else:
        print("Transaction not found.")

def display_savings_goals():
    goals = session.query(SavingsGoal).all()
    data = [(g.id, g.goal_name, g.target_amount) for g in goals]
    display_table(data, headers=["ID", "Goal Name", "Target Amount"])

def set_savings_goal():
    user_id = get_user_input("User ID: ", int)
    goal_name = get_user_input("Goal Name: ")
    target_amount = get_user_input("Target Amount: ", float)
    goal = SavingsGoal(user_id=user_id, goal_name=goal_name, target_amount=target_amount)
    session.add(goal)
    session.commit()
    print("Savings goal added!")

def delete_savings_goal():
    display_savings_goals()
    goal_id = get_user_input("Enter the ID of the savings goal to delete: ", int)
    goal_to_delete = session.query(SavingsGoal).filter_by(id=goal_id).first()

    if goal_to_delete:
        session.delete(goal_to_delete)
        session.commit()
        print(f"Savings goal with ID {goal_id} has been deleted.")
    else:
        print("Savings goal not found.")

def add_transaction():
    print("\n--- Add a Transaction ---")
    user_id = get_user_input("User ID: ", int)
    description = get_user_input("Description: ")
    amount = get_user_input("Amount: ", float)
    date_str = get_user_input("Date (YYYY-MM-DD): ")

    try:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    # Create a new transaction
    transaction = Transaction(user_id=user_id, description=description, amount=amount, date=date)
    
    # Add the transaction to the session and commit
    session.add(transaction)
    session.commit()

    print("Transaction added!")

def add_user():
    print("\n--- Add a User ---")
    name = get_user_input("Name: ")
    email = get_user_input("Email: ")

    # Check if the email already exists in the database
    existing_user = session.query(User).filter_by(email=email).first()
    if existing_user:
        print(f"Error: The email '{email}' is already in use. Please try a different email.")
        return

    # Create a new user if the email is unique
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    print(f"User {name} added successfully!")

def delete_user():
    display_users()
    user_id = get_user_input("Enter the ID of the user to delete: ", int)
    user_to_delete = session.query(User).filter_by(id=user_id).first()

    if user_to_delete:
        session.delete(user_to_delete)
        session.commit()
        print(f"User with ID {user_id} has been deleted.")
    else:
        print("User not found.")

def display_users():
    users = session.query(User).all()
    data = [(u.id, u.name, u.email) for u in users]
    display_table(data, headers=["ID", "Name", "Email"])

if __name__ == "__main__":
    main_menu()
