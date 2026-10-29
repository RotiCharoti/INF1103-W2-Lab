import json
from product import Product
from inventory import Inventory

FILENAME = "inventory.json"


def save_inventory(inventory):
    data = [
        {"id": p.get_product_id(), "name": p.get_name(),
         "price": p.get_price(), "stock": p.get_stock()}
        for p in inventory.get_products()
    ]
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)


def load_inventory():
    inventory = Inventory()
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
        for item in data:
            inventory.add_product(
                Product(item["id"], item["name"], item["price"], item["stock"])
            )
    except FileNotFoundError:
        inventory.add_product(Product("P001", "Laptop", 1200.00, 15))
        inventory.add_product(Product("P002", "Mouse", 25.50, 40))
        inventory.add_product(Product("P003", "Keyboard", 45.00, 25))
        save_inventory(inventory)
    return inventory


def display_menu():
    print("\n----------- MENU ----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("---------------------------")


def add_product_option(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ").strip()
    name = input("Product Name: ").strip()
    try:
        price = float(input("Price: ").strip())
        stock = int(input("Stock Quantity: ").strip())
        product = Product(product_id, name, price, stock)
    except ValueError as e:
        print(f"Invalid input! {e}")
        return

    if inventory.add_product(product):
        print("Product added successfully!")
    else:
        print(f"A product with ID {product_id} already exists.")


def update_stock_option(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)

    if product is None:
        print("No product found.")
        return

    print("Product Found:")
    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}\n")
    try:
        new_stock = int(input("New Stock Quantity: ").strip())
        product.update_stock(new_stock)
        print("\nStock updated successfully!")
    except ValueError as e:
        print(f"Invalid input! {e}")


def search_product_option(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)
    if product is None:
        print("No product found.")
    else:
        product.display_information()


# ---------------- Main program ----------------
def main():
    inventory = load_inventory()

    while True:
        display_menu()
        choice = input("\nEnter option: ").strip()

        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            add_product_option(inventory)
        elif choice == "3":
            update_stock_option(inventory)
        elif choice == "4":
            search_product_option(inventory)
        elif choice == "5":
            print("Saving inventory...")
            save_inventory(inventory)
            print(f"Inventory saved successfully to {FILENAME}.")
        elif choice == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully.")
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option! Please enter a valid option (1-6).")


if __name__ == "__main__":
    main()