from src import Food

def test_food_init():
    f = Food("Salad", 250.0, True)
    assert f.name == "Salad"
    assert f.get_price() == 250.0
    assert f.is_vegetarian is True