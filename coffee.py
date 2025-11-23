from typing import List

class Coffee:
    """Represents a coffee product."""

    _all: List['Coffee'] = []

    def __init__(self, name: str):
        self._name = None
        self.name = name
        Coffee._all.append(self)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string")

        value = value.strip()
        if not (3 <= len(value) <= 30):
            raise ValueError("Coffee name must be between 3 and 30 characters")

        self._name = value

    def orders(self):
        from order import Order
        return [o for o in Order._all if o.coffee is self]

    def customers(self):
        return list({o.customer for o in self.orders()})

    def num_orders(self) -> int:
        """Return the number of orders for this coffee."""
        return len(self.orders())

    def average_price(self) -> float:
        """Return the average price for this coffee across all orders."""
        orders = self.orders()
        if not orders:
            return 0.0
        total = sum(o.price for o in orders)
        return total / len(orders)

    @classmethod
    def most_ordered(cls):
        from order import Order
        if not Order._all:
            return None

        counts = {}
        for o in Order._all:
            counts[o.coffee] = counts.get(o.coffee, 0) + 1

        return max(counts, key=counts.get)

    def __repr__(self):
        return f"<Coffee name={self.name!r}>"
