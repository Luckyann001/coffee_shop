# debug.py
from customer import Customer
from coffee import Coffee
from order import Order

# clear any previous orders
Order._all.clear()

if __name__ == "__main__":
    alice = Customer("Alice")
    bob = Customer("Bob")

    espresso = Coffee("Espresso")
    latte = Coffee("Latte")

    alice.create_order(espresso, 3.5)
    alice.create_order(latte, 4.0)
    bob.create_order(espresso, 5.0)
    bob.create_order(espresso, 2.5)

    print("All orders:", Order._all)
    print("Espresso num_orders:", espresso.num_orders())
    print("Espresso avg price:", espresso.average_price())
    print("Espresso customers:", espresso.customers())
    print("Alice coffees:", alice.coffees())
    print("Most aficionado for espresso:", Customer.most_aficionado(espresso))
