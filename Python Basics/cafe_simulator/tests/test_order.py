from src import Order
from src import Food

def test_add_item_and_total_price():
    order = Order()
    food_item = Food("Burger", 300.0, False)
    order.add_item(food_item)
    assert order.total_price() == 300.0

def test_process_order(capsys):
    order = Order()
    order.add_item(Food("Pizza", 450.0, False))
    order.process_order()
    captured = capsys.readouterr()
    assert "Pizza" in captured.out