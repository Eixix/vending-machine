from models.Item import Item


class VendingMachine:
    def __init__(self):
        self.total_capacity = 0
        self.items = {}

    def print_all_items(self):
        for item in self.items.values():
            print(item)

    def add_item(self, item: Item):
        if item.name in self.items:
            return ("error", "An item of this kind is already present. Please use another name.")
        if self.total_capacity >= 10:
            return ("error", "The maximum capacity of the vending is already reached.")
        self.items[item.name] = item
        return ("success", f"Item {item.name} was added successfully. Please add stock for this item.")

    def restock_item(self, item_name: str, additional_items: int):
        item = self.items.get(item_name)

        if not item or item.name not in self.items:
            return ("error", "This item is not available for restock, please choose a valid item.")
        if int(self.items[item.name].amount) + additional_items >= 10:
            return ("error", "With the items you added the maximum total capacity is exceeded!")
        self.items[item.name].amount += additional_items
        return ("success", f"Item {item.name} has been restocked to a total of {self.items[item.name] + additional_items}")

    def delete_item(self, item_name: str):
        item = self.items.get(item_name)
        if not item or item.name not in self.items:
            return ("error", "This item is not available for deletion, please choose a valid item.")
        self.items.pop(item_name)
        return ("success", f"Item {item_name} has been deleted")