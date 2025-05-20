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
        from order import Order
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
