import json
from digital_product import DigitalProduct
from inventory import Inventory
from physical_product import PhysicalProduct

FILENAME = "inventory.json"

def product_to_dictionary(product):
    common_data = {
        "id": product.get_product_id(),
        "name": product.get_name(),
        "price": product.get_price(),
        "stock": product.get_stock()
    }

    if isinstance(product, PhysicalProduct):
        common_data["type"] = "physical"
        common_data["weight"] = product.get_weight()
    elif isinstance(product, DigitalProduct):
        common_data["type"] = "digital"
        common_data["download_size"] = product.get_download_size()
    else:
        raise TypeError("Unknown product type.")

    return common_data


def save_inventory(inventory):
    data = [
        product_to_dictionary(product)
        for product in inventory.get_products()
    ]

    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def load_inventory():
    inventory = Inventory()

    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            data = json.load(file)

        for item in data:
            product_type = item.get("type")

            if product_type == "physical":
                product = PhysicalProduct(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["weight"]
                )
            elif product_type == "digital":
                product = DigitalProduct(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["download_size"]
                )
            else:
                print(
                    f"Skipping product {item.get('id', 'unknown')}: "
                    "missing or invalid product type."
                )
                continue

            inventory.add_product(product)

    except FileNotFoundError:
        # Create sample data if inventory file does not exist
        inventory.add_product(
            PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.5)
        )
        inventory.add_product(
            PhysicalProduct("P002", "Mouse", 25.50, 40, 0.2)
        )
        inventory.add_product(
            DigitalProduct("D001", "Antivirus Software", 39.90, 100, 250)
        )
        save_inventory(inventory)

    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        print(f"Unable to load inventory data: {error}")
        print("Starting with an empty inventory.")

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
    print("\nSelect Product Type")
    print("1. Physical Product")
    print("2. Digital Product")

    choice = input("Enter option: ").strip()

    if choice not in ("1", "2"):
        print("Invalid product type. Please enter 1 or 2.")
        return

    try:
        product_id = input("Product ID: ").strip()
        name = input("Product Name: ").strip()
        price = float(input("Price: ").strip())
        stock = int(input("Stock Quantity: ").strip())

        if choice == "1":
            weight = float(input("Weight (kg): ").strip())
            product = PhysicalProduct(
                product_id, name, price, stock, weight
            )
        else:
            download_size = float(input("Download Size (MB): ").strip())
            product = DigitalProduct(
                product_id, name, price, stock, download_size
            )

    except ValueError as error:
        print(f"Invalid input! {error}")
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

    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}")

    try:
        new_stock = int(input("New Stock Quantity: ").strip())
        product.update_stock(new_stock)
        print("Stock updated successfully!")
    except ValueError as error:
        print(f"Invalid input! {error}")

def search_product_option(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)

    if product is None:
        print("No product found.")
    else:
        print(product.display_information())
        print(product.get_fulfilment_info())

        if isinstance(product, PhysicalProduct):
            print(
                f"Shipping Cost: "
                f"${product.calculate_shipping_cost():.2f}"
            )

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
            save_inventory(inventory)
            print(f"Inventory saved successfully to {FILENAME}.")
        elif choice == "6":
            save_inventory(inventory)
            print("Inventory saved successfully.")
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option! Please enter a valid option (1-6).")


if __name__ == "__main__":
    main()
