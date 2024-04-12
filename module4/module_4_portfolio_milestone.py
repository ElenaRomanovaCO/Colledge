# Creating ItemToPurchase class
class ItemToPurchase:

    def __init__(self, name="", price=0.0, quantity=0):
        self.item_name = name
        self.item_price = price  # float
        self.item_quantity = quantity  # int


# Creating Main function
def main():
    print("Item 1")

    name = input("Enter the item name: ")
    price = float(input("Enter the item price: "))
    quantity = int(input("Enter the item quantity: "))
    item1 = ItemToPurchase(name, price, quantity)


    print("Item 2")

    name = input("Enter the item name: ")
    price = float(input("Enter the item price: "))
    quantity = int(input("Enter the item quantity: "))
    item2 = ItemToPurchase(name, price, quantity)

    total_price = ((float(item1.item_price) * int(item1.item_quantity)) +
                   (float(item2.item_price) * int(item2.item_quantity)))
    print(f"{total_price=}")


# Calling Main function
main()