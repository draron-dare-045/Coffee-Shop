from customer import Customer
from coffee import Coffee

class Order:
    # Class-level list to store all Order instances
    _all_orders = []
    # Initializes an Order with customer, coffee, and price after validating their types and values
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance.")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance.")
        if not isinstance(price, float):
            raise TypeError("price must be a float.")
        # checks if price is within the range and if not throws an error
        if not (1.0 <= price <= 10.0):
            raise ValueError("price must be between 1.0 and 10.0.")
        
        # Stores validated values as private attributes and appends this order to the class-level order list
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order._all_orders.append(self)

    # Returns the value of the private attribute _customer using the @property decorator
    @property
    def customer(self):
        return self._customer

    # Returns the value of the private attribute _coffee using the @property decorator
    @property
    def coffee(self):
        return self._coffee

    # Returns the value of the private attribute _price using the @property decorator
    @property
    def price(self):
        return self._price

    # Prevents modification of price after order creation
    @price.setter
    def price(self):
        raise AttributeError("Price is immutable.")
    
    # Returns all the orders
    @classmethod
    def all(cls):
        return cls._all_orders
