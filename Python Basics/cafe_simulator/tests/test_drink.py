from src import Drink

def test_drink_init():
    d = Drink("Latte", 3.5, "hot")
    assert d.name == "Latte"
    assert d.get_price() == 3.5
    assert d.temperature == "hot"