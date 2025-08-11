class MenuItem:
    """
    Base class for menu items.

    Attributes:
        name (str): Name of the menu item.
        _price (float): Price of the menu item (private attribute) in UAH.
    """
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self._price = price

    def get_price(self) -> float:
        """Return the price of the item."""
        return self._price

    def prepare(self) -> None:
        """Prepare the item (to be overridden by subclasses)."""
        raise NotImplementedError("Subclasses must implement prepare() method")


class Drink(MenuItem):
    """
    Drink menu item.

    Attributes:
        temperature (str): 'hot' or 'cold'.
    """
    def __init__(self, name: str, price: float, temperature: str) -> None:
        super().__init__(name, price)
        self.temperature = temperature

    def prepare(self) -> None:
        """Prepare the drink."""
        print(f"Pouring the {self.temperature} drink: {self.name}")


class Food(MenuItem):
    """
    Food menu item.

    Attributes:
        is_vegetarian (bool): Whether the food is vegetarian.
    """
    def __init__(self, name: str, price: float, is_vegetarian: bool) -> None:
        super().__init__(name, price)
        self.is_vegetarian = is_vegetarian

    def prepare(self) -> None:
        """Prepare the food."""
        print(f"Cooking {'vegetarian' if self.is_vegetarian else 'non-vegetarian'} dish: {self.name}")