from customer import Customer
from coffee import Coffee
from order import Order

alice = Customer("Alice")
latte = Coffee("Latte")

alice.create_order(latte, 4.5)
alice.create_order(latte, 5.0)

print(latte.num_orders())       # Output: 2
print(latte.average_price())    # Output: 4.75
