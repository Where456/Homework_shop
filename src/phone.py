from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        elif isinstance(other, Phone):
            return self.quantity + other.quantity
        else:
            raise TypeError("Unsupported type for addition")

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def number_of_sim(self):
        return self.number_of_sim
