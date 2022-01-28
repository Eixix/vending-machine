from Item import Item

class Snack(Item):
    def __init__(self, name: str, price: int, weight: int, amount: int = 0):
        super().__init__(name, price, amount)
        self.weight = weight

    def __str__(self):
        return f"{self.name}: {self.price}€, {self.weight}gr, {self.amount} items"