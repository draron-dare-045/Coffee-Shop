from models import Customer, Coffee, Order


alice = Customer("Alice")
latte = Coffee("Latte")

alice.create_order(latte, 4.5)
alice.create_order(latte, 5.0)

print(latte.num_orders())       
print(latte.average_price())    
