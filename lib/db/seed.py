from lib.db.models import User, Transaction, SavingsGoal, session
from datetime import datetime

def seed_data():
    # Add users
    # user1 = User(name="Quincy Mike", email="quincy@gmail.com")
    # user2 = User(name="Joptham", email="joptham@gmail.com")
    user3 = User(name="Sean Daniel", email="Sean@gmail.com")
    user4 = User(name="Clark Kent", email="Clark@gmail.com")

    session.add_all([user3, user4])
    session.commit()

    # Add transactions
    # transaction1 = Transaction(user_id=1, description="Grocery shopping", amount=150.50, date=datetime(2024, 12, 1))
    # transaction2 = Transaction(user_id=2, description="Car repair", amount=500.00, date=datetime(2024, 12, 5))

    session.add_all([])
    session.commit()

    # Add savings goals
    # goal1 = SavingsGoal(user_id=1, goal_name="Vacation Fund", target_amount=2000.00,)
    # goal2 = SavingsGoal(user_id=2, goal_name="Emergency Fund", target_amount=3000.00,)

    session.add_all([])
    session.commit()

    print("Seed data added!")

if __name__ == "__main__":
    seed_data()
