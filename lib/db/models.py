from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()
engine = create_engine("sqlite:///finance_tracker.db")
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    transactions = relationship("Transaction", back_populates="user")
    savings_goals = relationship("SavingsGoal", back_populates="user")

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    description = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    user = relationship("User", back_populates="transactions")

class SavingsGoal(Base):
    __tablename__ = "savings_goals"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    goal_name = Column(String, nullable=False)
    target_amount = Column(Float, nullable=False)
    user = relationship("User", back_populates="savings_goals")

Base.metadata.create_all(engine)
