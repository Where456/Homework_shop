from src.item import Item


class LanguageMixin:
    LANGUAGES = ['EN', 'RU']

    def __init__(self):
        self._language = 'EN'

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'


class Keyboard(Item, LanguageMixin):
    def __init__(self, name: str, price: float, quantity: int):
        Item.__init__(self, name, price, quantity)
        LanguageMixin.__init__(self)

    def __str__(self):
        return self.name
