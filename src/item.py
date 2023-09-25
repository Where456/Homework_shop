class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self) -> None:
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            lines = lines[1:]
            for line in lines:
                data = line.strip().split(',')
                name = data[0]
                price = float(data[1])
                quantity = int(data[2])
                item = cls(name, price, quantity)
        return cls.all

    @staticmethod
    def string_to_number(string: str):
        try:
            number = int(float(string))
            return number
        except ValueError:
            return None


