from src.keyboard import Keyboard


def test_keyboard_initialization():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"


def test_keyboard_default_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb.language) == "EN"


def test_keyboard_change_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert str(kb.language) == "RU"

    kb.change_lang()
    assert str(kb.language) == "EN"


def test_keyboard_set_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.language = 'RU'
    assert str(kb.language) == "RU"
