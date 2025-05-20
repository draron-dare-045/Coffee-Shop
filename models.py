class Customer():
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance (value, str):
            raise TypeError("Name must be a string.")
        if not(1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters.")
        self._name = value
    
    def orders(self):
        return[order for order in Order.all() if order.customer == self]
    
    def coffees(self):
        return list ({order.coffee for order in self.orders()})
    
    def create_order( self, coffee, price):
        return (self, coffee, price)
    
from order import Order
class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("The name must be a string.")
        if len(name) < 3:
            raise ValueError("Name must be at leat 3 characters long")
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self):
        raise AttributeError("Coffe is immutable and therefore cannot be changed")
    
    def orders(self):
        return [order for order in Order.all() if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        return sum(order.price for order in orders) / len(orders)

from customer import Customer
from coffee import Coffee

class Order:
    _all_orders = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance.")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance.")
        if not isinstance(price, float):
            raise TypeError("price must be a float.")
        if not (1.0 <= price <= 10.0):
            raise ValueError("price must be between 1.0 and 10.0.")

        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order._all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        raise AttributeError("Price is immutable.")

    @classmethod
    def all(cls):
        return cls._all_orders
