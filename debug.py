from customer import Customer
from coffee import Coffee
from order import Order

# Create Customers
customer1 = Customer("Aron")
customer2 = Customer("Jane")
customer3 = Customer("Mike")

# Create Coffees
coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")
coffee3 = Coffee("Cappuccino")

# Create Orders
customer1.create_order(coffee1, 4.5)
customer1.create_order(coffee2, 5.0)
customer1.create_order(coffee1, 3.5)

customer2.create_order(coffee1, 6.0)
customer2.create_order(coffee2, 4.0)

customer3.create_order(coffee3, 5.5)

# Test: Customer orders
print(f"{customer1.name}'s orders: {[order.coffee.name for order in customer1.orders()]}")
print(f"{customer1.name}'s unique coffees: {[coffee.name for coffee in customer1.coffees()]}")

# Test: Coffee methods
print(f"{coffee1.name} number of orders: {coffee1.num_orders()}")
print(f"{coffee1.name} average price: {coffee1.average_price():.2f}")
print(f"{coffee2.name} number of orders: {coffee2.num_orders()}")
print(f"{coffee3.name} average price: {coffee3.average_price():.2f}")

# Test: Most aficionado for each coffee
aficionado1 = Customer.most_aficionado(coffee1)
aficionado2 = Customer.most_aficionado(coffee2)
aficionado3 = Customer.most_aficionado(coffee3)

print(f"Most aficionado of {coffee1.name}: {aficionado1.name if aficionado1 else 'None'}")
print(f"Most aficionado of {coffee2.name}: {aficionado2.name if aficionado2 else 'None'}")
print(f"Most aficionado of {coffee3.name}: {aficionado3.name if aficionado3 else 'None'}")

# Optional: List all orders
print("\nAll orders:")
for order in Order.all():
    print(f"{order.customer.name} ordered {order.coffee.name} for ${order.price:.2f}")
from customer import Customer
from coffee import Coffee

c1 = Customer("Aron")
coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")

c1.create_order(coffee1, 5.0)
c1.create_order(coffee1, 4.5)
c1.create_order(coffee2, 6.0)

print(coffee1.num_orders())         
print(coffee1.average_price())     
print(coffee2.num_orders())        
print(coffee2.average_price())     
