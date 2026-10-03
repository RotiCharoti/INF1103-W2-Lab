import json

filename = "inventory.json"

def display_menu():
    print("\n----------- MENU ----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("---------------------------")

def display_inventory(inventory):
    print("\nCurrent Inventory")
    print("------------------------------------------------")
    for item in inventory:
        print(f"ID: {item['id']} | Name: {item['name']} | Price: ${item['price']:.2f} | Stock: {item['stock']}")

def load_inventory():
    try:
        with open(filename, "r") as f:
            inventory = json.load(f)
    except FileNotFoundError:
        inventory = [ 
            {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
            {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
            {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25}
        ]
        with open(filename, "w") as file:
            json.dump(inventory, file, indent = 4)
    return inventory    

def save_inventory(inventory):
    with open(filename, "w") as file:
        json.dump(inventory, file, indent = 4)

def add_product():
    print("\nAdd New Product")
    id = input("Product ID: ").strip()
    name = input("Product Name: ").strip()
    try:
        price = float(input("Price: ").strip())
        if price < 0:
            print("Product price cannot be less than 0!")
            return
    except ValueError:
        print("Invalid input! Please enter a valid price for the product.")
        return
    try:
        stock = int(input("Stock Quantity: ").strip())
        if price < 0:
            print("Stock quantity cannot be less than 0!")
            return
    except ValueError:
        print("Invalid input! Please enter a valid quantity for the stock quantity.")
        return

    new_product = {
        "id": id,
        "name": name,
        "price": price,
        "stock": stock
    }

    current_inventory = load_inventory()
    current_inventory.append(new_product)
    save_inventory(current_inventory)
    print("Product added successfully\ns!")

def update_stock():
    print("\nUpdate Stock")
    id = input("Enter Product ID: ").strip()

    current_inventory = load_inventory()
    id_found = False

    for item in current_inventory:
        if item['id'] == id:
            id_found == True 
            print(f"Product Found: ")
            print(f"Name: {item['name']}")
            print(f"Current Stock: {item['stock']}\n")

            try:
                new_stock = int(input("New Stock Quantity: ").strip())
                if new_stock < 0:
                    print("Stock quantity cannot be less than 0.")
                    return
                item['stock'] = new_stock
                save_inventory(current_inventory)
                print("\nStock updated successfully!")
            except ValueError:
                print("Invalid input! Please enter a valid intger for the stock quantity.")
            break
    
    if not id_found:
        print(f"No product found.")

def search_product():
    print("\nSearch Product")
    target_id = input("Enter Product ID: ").strip()
    
    current_inventory = load_inventory()
    id_found = False
    
    for i in range(len(current_inventory)):
        if current_inventory[i]['id'] == target_id:
            print(f"ID: {current_inventory[i]['id']} | Name: {current_inventory[i]['name']} | Price: ${current_inventory[i]['price']:.2f} | Stock: {current_inventory[i]['stock']}")
            id_found = True  
            break           

    if not id_found:
        print("No product found.")
            
def main():
    while True:
        display_menu()
        choice = input("\nEnter option: ").strip()

        if choice == "1":
            inventory = load_inventory()
            display_inventory(inventory)
        
        elif choice == "2":
            add_product()

        elif choice == "3":
            update_stock()

        elif choice == "4":
            search_product()

        elif choice == "5":
            current_invetory = load_inventory()
            save_inventory(current_invetory)
            print("Saving inventory...")
            print("Inventory saved successfully to inventory.json.")

        elif choice == "6":
            print("Saving inventory before exit...")
            print("Inventory saved successfully.")
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option! Please enter a valid option (1-6).")
    
main()