class GroceryStore:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, quantity, price):
        if item_name in self.inventory:
            print(f"{item_name} already exists in the inventory. Use update to modify quantity or price.")
        else:
            self.inventory[item_name] = {'quantity': quantity, 'price': price}
            print(f"{quantity} {item_name}(s) added to the inventory at Rs.{price} each.")

    def update_item(self, item_name, quantity=None, price=None):
        if item_name in self.inventory:
            if quantity is not None:
                self.inventory[item_name]['quantity'] += quantity
                print(f"{quantity} {item_name}(s) added to the inventory.")
            if price is not None:
                self.inventory[item_name]['price'] = price
                print(f"Price for {item_name} updated to Rs.{price}.")
        else:
            print(f"{item_name} does not exist in the inventory. Use add to add a new item.")

    def view_inventory(self):
        print("Current Inventory:")
        for item_name, details in self.inventory.items():
            print(f"{item_name}: Quantity - {details['quantity']}, Price - Rs.{details['price']} each")

    def remove_item(self, item_name):
        if item_name in self.inventory:
            del self.inventory[item_name]
            print(f"{item_name} removed from the inventory.")
        else:
            print(f"{item_name} does not exist in the inventory.")

def main():
    grocery_store = GroceryStore()

    while True:
        print("\nGrocery Store Inventory Management")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Remove Item")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            grocery_store.add_item(name, quantity, price)

        elif choice == '2':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity to add (0 to skip): "))
            price = float(input("Enter new price (0.0 to skip): "))
            grocery_store.update_item(name, quantity, price)

        elif choice == '3':
            grocery_store.view_inventory()

        elif choice == '4':
            name = input("Enter item name to remove: ")
            grocery_store.remove_item(name)

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
