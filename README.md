This project models a simple coffee shop using Object-Oriented Programming (OOP) principles.
It includes three main classes:

Customer

Coffee

Order

The goal is to understand class relationships, single source of truth, and data modeling in Python.

 Domain Model
Customer 1 --- * Order * --- 1 Coffee

Entities & Relationships

A Customer can have many Orders.

A Coffee type can appear in many Orders.

An Order belongs to one Customer and one Coffee.

Single Source of Truth

The Order class keeps a class-level list (Order.all) of all Order instances.
This ensures all objects derive their relationships from one shared source.

Class Responsibilities
Customer

Represents a customer in the coffee shop.

Attributes

name

Key Methods

orders() → List of orders made by this customer

coffees() → Unique coffees the customer has ordered

create_order(coffee, price) → Creates & stores a new order

Coffee

Represents a coffee type.

Attributes

name

Key Methods

orders() → All orders for this coffee

customers() → All customers who ordered this coffee

num_orders() → Count of orders for this coffee

average_price() → Average amount customers pay

most_aficionado() → Customer who spent the most on this coffee

Order

Represents a purchase of a coffee by a customer.

Attributes

customer

coffee

price

Class Attribute (Single Source of Truth)

Order.all = []

▶ Running the Project (Debug Mode)

A debug.py file is included so you can manually test the relationships.

Run:

python3 debug.py


Expected output includes:

All orders

Coffee stats

Customer purchase info

Most aficionado customer


 Project Structure
coffee_shop/
│
├── customer.py
├── coffee.py
├── order.py
│
├── debug.py
├── README.md
│
└── tests/
    ├── test_customer.py
    ├── test_coffee.py
    └── test_order.py

 What I Learned

✔ How to design a domain model
✔ Class relationships in OOP
✔ How to maintain a single source of truth
✔ Writing methods that compute values dynamically


Author

Luckyann Kagendo — Moringa School Phase 3
Python | OOP | Software Development