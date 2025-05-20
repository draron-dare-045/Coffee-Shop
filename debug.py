from customer import Customer
from coffee import Coffee

# Create instances
alice = Customer("Alice")
latte = Coffee("Latte")

# Create orders
alice.create_order(latte, 3.5)
alice.create_order(latte, 4.0)

# Print results
print(f"Orders for {alice.name}: {[o.price for o in alice.orders()]}")
print(f"{latte.name} has {latte.num_orders()} orders")
print(f"Average price for {latte.name}: {latte.average_price():.2f}")
