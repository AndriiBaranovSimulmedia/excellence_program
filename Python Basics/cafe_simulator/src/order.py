from typing import List
from .menu_items import MenuItem

class Order:
    """
    Represents a customer's order.

    Attributes:
        items (List[MenuItem]): List of menu items in the order.
    """
    def __init__(self) -> None:
        self.items: List[MenuItem] = []

    def add_item(self, item: MenuItem) -> None:
        """Add a menu item to the order."""
        self.items.append(item)

    def total_price(self) -> float:
        """Calculate the total price of the order."""
        return sum(item.get_price() for item in self.items)

    def process_order(self) -> None:
        """Prepare all items in the order."""
        print("\n--- Processing Order ---")
        for item in self.items:
            item.prepare()
        print(f"Total price: UAH {self.total_price():.2f}")
