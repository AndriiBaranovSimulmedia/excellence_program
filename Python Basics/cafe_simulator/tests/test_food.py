from src import Food

def test_food_init():
    f = Food("Salad", 5.0, True)
    assert f.name == "Salad"
    assert f.get_price() == 5.0
    assert f.is_vegetarian is True