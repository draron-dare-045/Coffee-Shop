class Customer():
    # Initialises the customer name as a private attribute
    def __init__(self, name):
        self.name = name
    
    # Returns the value of the private attribute _name using the @property decorator
    @property
    def name(self):
        return self._name
    
    # Validates and sets the _private attribute
    @name.setter
    def name(self, value):
        # Checks if value inputed is a string and raises an error otherwise
        if not isinstance (value, str):
            raise TypeError("Name must be a string.")
        # Checks if the value inputed length is not more than 15 characters and not less than 1 character long and raises an error if so
        if not(1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters.")
        # Stores the validated name
        self._name = value
    
    # Returns a list of orders of a respective customer which is stored in an object found in the class order in a file Order.py
    def orders(self):
        from order import Order
        return[order for order in Order.all() if order.customer == self]
    
    # Returns a list of unique coffees this customer has ordered 
    def coffees(self):
        return list ({order.coffee for order in self.orders()})
    
    # This just returns an Order with a customer name price and the coffee from the order object
    def create_order( self, coffee, price):
        from order import Order
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        # Dictionary to keep track of customer spending on the given coffee
        spending = {}

        for order in Order.all():
            if order.coffee == coffee:
                customer = order.customer
                spending[customer] = spending.get(customer, 0) + order.price

        # Return the customer who spent the most, or None if no spending
        if not spending:
            return None
        return max(spending, key=spending.get)