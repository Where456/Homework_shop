from src.item import Item


def test_calculate_total_price():
    item = Item("Товар 1", 10.0, 5)
    assert item.calculate_total_price() == 50.0


def test_apply_discount():
    item = Item("Товар 2", 20.0, 3)
    Item.pay_rate = 0.9
    item.apply_discount()
    assert item.price == 18.0
