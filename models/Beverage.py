from models.Item import Item

class Beverage(Item):
    def __init__(self, name: str, price: int, volume: int, amount: int = 0):
        super().__init__(name, price, amount)
        self.volume = volume

    def __str__(self):
        print(f"{self.name}: {self.price}€, {self.volume}ml, {self.amount} items")