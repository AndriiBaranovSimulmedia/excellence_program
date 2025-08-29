from src import Drink

def test_drink_init():
    d = Drink("Latte", 90, "hot")
    assert d.name == "Latte"
    assert d.get_price() == 90
    assert d.temperature == "hot"