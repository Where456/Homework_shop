import pytest

from src.item import Item
from src.phone import Phone


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


def test_addition():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)

    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10


def test_phone_initialization():
    phone = Phone("Samsung Galaxy", 500, 10, 2)
    assert phone.name == "Samsung Galaxy"
    assert phone.price == 500
    assert phone.quantity == 10
    assert phone.number_of_sim == 2


def test_phone_set_number_of_sim():
    phone = Phone("iPhone", 800, 5, 1)
    phone.number_of_sim = 2
    assert phone.number_of_sim == 2


def test_phone_set_invalid_number_of_sim():
    phone = Phone("Google Pixel", 600, 3, 1)
    with pytest.raises(ValueError):
        phone.number_of_sim = -1
