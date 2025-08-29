from typing import List
from menu_items import MenuItem
from order import Order
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Customer:
    """
    Represents a customer in the cafe.

    Attributes:
        name (str): Customer's name.
    """
    def __init__(self, name: str) -> None:
        self.name = name

    def create_order(self, menu_items: List[MenuItem]) -> Order:
        """Create an order from a list of menu items."""
        order = Order()
        for item in menu_items:
            order.add_item(item)

        logger.info(f'Order created for {self.name}')
        return order