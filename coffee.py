class Coffee:
    
    _all_coffees = []
    # Initialize 
    def __init__(self, name):
        # Checks if the data type of the name is a string if not throws an error
        if not isinstance(name, str):
            raise TypeError("The name must be a string.")
        # Checks if length of the imput is more than 3 characters long
        if len(name) < 3:
            raise ValueError("Name must be at leat 3 characters long")
        # Stores the validated name as a private attribute
        self._name = name
    
    # Returns the value of the private attribute _name using the @property decorator
    @property
    def name(self):
        return self._name
    
    # prevents setting of the coffee and passes an error message if one tries to alter the name.
    @name.setter
    def name(self, value):
        raise AttributeError("Coffee is immutable and therefore cannot be changed")
    
    # returns the a list of orders associated with this coffee
    def orders(self):
        from order import Order
        return [order for order in Order.all() if order.coffee == self]

    # returns the list of customers who ordered that particular coffee
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    # counts and returns the number of orders
    def num_orders(self):
        return len(self.orders())
    
    # returns the average price for orders
    def average_price(self):
        orders = self.orders()
        # if statement to check if there are orders.
        if not orders:
            return 0
        return sum(order.price for order in orders) / len(orders)
    
    @classmethod
    def all(cls):
        return cls._all_coffees