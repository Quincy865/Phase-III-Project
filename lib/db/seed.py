from lib.db.models import User, Transaction, SavingsGoal, session
from datetime import date

def seed_data():
    # Add users
    # user1 = User(name="John Doe", email="john@gmail.com")
    # user2 = User(name="Joptham", email="joptham@gmail.com")
    user3 = User(name="Samuel", email="samuel@gmail.com")

    session.add_all([user3])
    session.commit()

    # Add transactions
    # transaction1 = Transaction(user_id=1, description="Grocery shopping", amount=150.50, date=date(2024, 12, 1))
    # transaction2 = Transaction(user_id=2, description="Car repair", amount=500.00, date=date(2024, 12, 5))
    transaction3 = Transaction(user_id=3, description="Summer Tides", amount=550.30, date=date(2025, 7, 6))

    session.add_all([transaction3])
    session.commit()

    # Add savings goals
    # goal1 = SavingsGoal(user_id=1, goal_name="Vacation Fund", target_amount=2000.00, saved_amount=500.00)
    # goal2 = SavingsGoal(user_id=2, goal_name="Emergency Fund", target_amount=3000.00, saved_amount=1000.00)
    goal3 = SavingsGoal(user_id=3, goal_name="New Car", target_amount=20000.00, saved_amount=10000.00)

    session.add_all([goal3])
    session.commit()

    print("Seed data added!")

if __name__ == "__main__":
    seed_data()
