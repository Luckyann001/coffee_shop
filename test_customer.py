import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_validation():
    with pytest.raises(TypeError):
        Customer(123)

    with pytest.raises(ValueError):
        Customer("")

    with pytest.raises(ValueError):
        Customer("a" * 20)

    c = Customer("Alice")
    assert c.name == "Alice"


def test_customer_orders_relationship():
    c = Customer("Bob")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Mocha")

    o1 = c.create_order(coffee1, 4.5)
    o2 = c.create_order(coffee2, 5.0)

    assert o1 in c.orders()
    assert o2 in c.orders()


def test_customer_coffees_unique():
    c = Customer("Charlie")
    coffee = Coffee("Espresso")

    c.create_order(coffee, 3.0)
    c.create_order(coffee, 4.0)

    assert len(c.coffees()) == 1
    assert c.coffees()[0].name == "Espresso"


def test_most_aficionado():
    # reset order list
    Order._all.clear()

    alice = Customer("Alice")
    bob = Customer("Bob")
    espresso = Coffee("Espresso")

    alice.create_order(espresso, 3.0)
    bob.create_order(espresso, 5.0)
    bob.create_order(espresso, 4.0)

    assert Customer.most_aficionado(espresso) == bob
