from src.customer import Customer
from src.menu_items import Food

def test_create_order():
    customer = Customer("Alice")
    pizza = Food("Pizza", 8.0, False)
    order = customer.create_order([pizza])
    assert order.total_price() == 8.0