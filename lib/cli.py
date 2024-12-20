from lib.db.models import User, Transaction, SavingsGoal, session
from lib.helpers import display_table, get_user_input

def main_menu():
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. View Transactions")
        print("2. Add a Transaction")
        print("3. Delete a Transaction")
        print("4. View Savings Goals")
        print("5. Set a Savings Goal")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            display_transactions()
        elif choice == "2":
            add_transaction()
        elif choice == "3":
            delete_transaction()
        elif choice == "4":
            display_savings_goals()
        elif choice == "5":
            set_savings_goal()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def display_transactions():
    transactions = session.query(Transaction).all()
    data = [(t.id, t.description, t.amount, t.date) for t in transactions]
    display_table(data, headers=["ID", "Description", "Amount", "Date"])

def add_transaction():
    user_id = get_user_input("User ID: ", int)
    description = get_user_input("Description: ")
    amount = get_user_input("Amount: ", float)
    date = get_user_input("Date (YYYY-MM-DD): ")
    transaction = Transaction(user_id=user_id, description=description, amount=amount, date=date)
    session.add(transaction)
    session.commit()
    print("Transaction added!")

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

def display_savings_goals():
    goals = session.query(SavingsGoal).all()
    data = [(g.id, g.goal_name, g.target_amount, g.saved_amount) for g in goals]
    display_table(data, headers=["ID", "Goal Name", "Target Amount", "Saved Amount"])

def set_savings_goal():
    user_id = get_user_input("User ID: ", int)
    goal_name = get_user_input("Goal Name: ")
    target_amount = get_user_input("Target Amount: ", float)
    goal = SavingsGoal(user_id=user_id, goal_name=goal_name, target_amount=target_amount, saved_amount=0.0)
    session.add(goal)
    session.commit()
    print("Savings goal added!")

if __name__ == "__main__":
    main_menu()
