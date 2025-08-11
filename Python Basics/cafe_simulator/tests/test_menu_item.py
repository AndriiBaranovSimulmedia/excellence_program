import pytest
from src import MenuItem

class DummyItem(MenuItem):
    def prepare(self):
        return f"Preparing {self.name}"

def test_get_price():
    item = DummyItem("Test Item", 10.0)
    assert item.get_price() == 10.0

def test_prepare():
    item = DummyItem("Test", 5.0)
    assert item.prepare() == "Preparing Test"

def test_prepare_not_implemented():
    base_item = MenuItem("Base", 5.0)
    with pytest.raises(NotImplementedError):
        base_item.prepare()