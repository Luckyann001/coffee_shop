Coffee Shop OOP Domain Model

This project models a Coffee Shop domain using Object-Oriented Programming (OOP) in Python.
It includes three main classes:

Customer

Coffee

Order

These classes demonstrate relationships, validation, class methods, and object interaction.

Project Structure
coffee_shop/
│── customer.py
│── coffee.py
│── order.py
│── debug.py
│── README.md
└── tests/ (optional for bonus)
     ├── test_customer.py
     ├── test_coffee.py
     └── test_order.py

Domain Overview
Customer

Has a name (1–15 characters)

Can place many orders

Can order many different coffees (many-to-many through Order)

Methods:

orders()

coffees()

create_order(coffee, price)

most_aficionado(coffee) (class method)

Coffee

Has a name (3+ characters)

Can have many orders

Methods:

orders()

customers()

num_orders()

average_price()

Order

Connects a Customer and a Coffee

Has a price (1.0–10.0)

Belongs to one customer and one coffee

Stored in a global _all list

How to Run the Project

Create and activate a virtual environment:

pipenv install
pipenv shell


Run the debug script:

python3 debug.py


This prints example customers, coffees, orders, and method outputs.


If you added the optional tests:

Install pytest:

pipenv install pytest


Run tests:

pytest

🗂 Features Demonstrated

✔ Object-Oriented Programming
✔ Relationships (one-to-many, many-to-many)
✔ Data validation
✔ Class methods
✔ Aggregate methods
✔ Clean architecture
✔ Debugging script
✔ Optional testing

👤 Author

Created by Luckyann Kagendo as part of the Moringa School Phase 3 Python Assessment.