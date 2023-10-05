class LanguageMixin:
    LANGUAGES = ['EN', 'RU']

    def __init__(self):
        self._language = 'EN'

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        if value in self.LANGUAGES:
            self._language = value
        else:
            raise ValueError("Unsupported language")

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'


class Keyboard(LanguageMixin):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__()
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return self.name