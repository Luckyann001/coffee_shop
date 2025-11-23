from typing import List

class Order:
    """Represents an order linking a Customer and a Coffee with a price."""

    _all: List['Order'] = []

    def __init__(self, customer, coffee, price: float):
        # lazy import to avoid circular import at module import time
        from customer import Customer
        from coffee import Coffee

        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance")
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number")

        price = float(price)
        if not (1.0 <= price <= 10.0):
            raise ValueError("price must be between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = price

        # register the order
        Order._all.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self) -> float:
        return self._price

    def __repr__(self):
        return f"<Order customer={self.customer.name!r} coffee={self.coffee.name!r} price={self.price!r}>"
