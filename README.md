# Personal Finance Tracker CLI Application

## Overview
The **Personal Finance Tracker** is a command-line application designed to help users efficiently manage their personal finances. With this tool, users can record income and expenses, categorize transactions, and view detailed financial summaries. The application is built using Python fundamentals, SQLAlchemy ORM for database management, and follows a structured package organization.

## Features
- **Record Transactions:** Add income and expenses with details like amount, category, and description.
- **Categorize Transactions:** Organize transactions into customizable categories (e.g., Food, Rent, Entertainment).
- **View Summaries:** Generate reports showing total income, expenses, and net balance.
- **Transaction History:** View all transactions with filters for date range and category.
- **Interactive CLI:** User-friendly interface to navigate through features seamlessly.

## Technologies Used
Python
SQLite (managed with SQLAlchemy ORM)
Pipenv for virtual environment and dependency management

## Installation
### Prerequisites
Ensure you have the following installed on your system:
- Python 3.8+
- Pipenv

### Steps
1. Clone the repository:
2. Navigate to the project directory:
3. Install dependencies using Pipenv:
```bash
pipenv install
```
4. Activate the virtual environment:
```bash
pipenv shell
```
5. Initialize the database:
```bash
python initialize_db.py
```

## Usage
Run the application using:
```bash
python main.py
```

### Available Commands
- **Add Income:** Record an income transaction.
- **Add Expense:** Record an expense transaction.
- **View Summary:** Display financial reports.
- **Filter Transactions:** View specific transactions by category or date range.
- **Exit:** Exit the application.

## Database Schema
The application uses SQLAlchemy ORM to manage the database with the following schema:

- **Users**
- `id`: Primary key
- `name`: User's name

- **Transactions**
- `id`: Primary key
- `user_id`: Foreign key referencing Users
- `type`: Income or Expense
- `amount`: Transaction amount
- `category`: Transaction category
- `date`: Date of transaction

## Future Enhancements
- Add budget tracking and alerts for overspending.
- Include visualization tools like charts for income/expense trends.
- Allow exporting financial data to CSV or PDF.
- Multi-user support with authentication.

## Contributing
Contributions are welcome! If you have suggestions or want to contribute to the project:
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
```bash
git checkout -b feature-name
```
3. Commit your changes:
```bash
git commit -m "Add feature-name"
```
4. Push to your branch:
```bash
git push origin feature-name
```
5. Submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or feedback, feel free to reach out to:
- **Name:** Quincy Michael
- **Email:** quincymichael@gmail.com

---

Happy tracking! 💰