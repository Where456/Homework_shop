from src.item import Item


def test_calculate_total_price():
    item = Item("Товар 1", 10.0, 5)
    assert item.calculate_total_price() == 50.0


def test_apply_discount():
    item = Item("Товар 2", 20.0, 3)
    Item.pay_rate = 0.9
    item.apply_discount()
    assert item.price == 18.0


def test_string_to_number():
    assert Item.string_to_number("123") == 123
    assert Item.string_to_number("5.5") == 5
    assert Item.string_to_number("abc") is None


# def test_instantiate_from_csv():
#     items_data = Item.instantiate_from_csv('../src/items.csv')
#     assert len(items_data) == 5
#
#     assert items_data[0]['name'] == "Смартфон"
#     assert items_data[0]['price'] == 100
#     assert items_data[0]['quantity'] == 1
#
#     assert len(Item.all) == 5
#
#     item1 = Item.all[0]
#     assert item1.name == "Смартфон"
#     assert item1.price == 100
#     assert item1.quantity == 1

def test_item_repr():
    item = Item("Товар 1", 10.0, 5)
    assert repr(item) == "Item('Товар 1', 10.0, 5)"

def test_item_str():
    item = Item("Товар 1", 10.0, 5)
    assert str(item) == "Товар 1"
