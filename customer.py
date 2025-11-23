from typing import List, Optional
from order import Order
from coffee import Coffee

class Customer:
    def __init__(self, name: str):
        self._name = None
        self.name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string")
        value = value.strip()
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name must be between 1 and 15 characters")
        self._name = value

    def orders(self) -> List['Order']:
        """Return a list of Order instances placed by this customer."""
        return [o for o in Order._all if o.customer is self]

    def coffees(self) -> List['Coffee']:
        """Return a unique list of Coffee instances this customer has ordered."""
        coffees = [o.coffee for o in self.orders()]

        unique = []
        seen = set()
        for c in coffees:
            if c not in seen:
                unique.append(c)
                seen.add(c)
        return unique

    def create_order(self, coffee: 'Coffee', price: float) -> 'Order':
        """Create a new Order for this customer and the given Coffee."""
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee: 'Coffee') -> Optional['Customer']:
        """Return the Customer who spent the most on the provided coffee."""
        if not isinstance(coffee, Coffee):
            raise TypeError("Argument must be a Coffee instance")

        orders = [o for o in Order._all if o.coffee is coffee]
        if not orders:
            return None

        totals = {}
        for o in orders:
            totals[o.customer] = totals.get(o.customer, 0.0) + o.price

        best_customer = max(totals, key=totals.get)
        return best_customer

    def __repr__(self):
        return f"<Customer name={self.name!r}>"
