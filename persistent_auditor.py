def load_inventory():
    orders = []

    file_exists = True
    try:
        f = open("inventory.txt", "r")
        f.close()
    except FileNotFoundError:
        file_exists = False

    if file_exists:
        f = open("inventory.txt", "r")
        lines = f.read().strip().split("\n")
        f.close()
        for line in lines:
            if line.strip() != "" and not line.startswith("TOTAL"):
                parts = line.split(",")
                if len(parts) == 3:
                    order_id = parts[0].strip()
                    name = parts[1].strip()
                    quantity = int(parts[2].strip())
                    orders.append([order_id, name, quantity])

    return orders


def save_inventory(orders_list):
    f = open("inventory.txt", "w")
    total = 0
    for order in orders_list:
        f.write(order[0] + ", " + order[1] + ", " + str(order[2]) + "\n")
        total += order[2]
    f.write("TOTAL, " + str(total) + "\n")
    f.close()


def get_next_order_id(orders_list):
    if len(orders_list) == 0:
        return "1001"
    last_id = orders_list[-1][0]
    return str(int(last_id) + 1)


def display_current_orders(orders_list):
    print("")
    print("Current Orders:")
    print("")
    for order in orders_list:
        print(order[0] + ", " + order[1] + ", " + str(order[2]))
    print("")


def get_product_name():
    while True:
        name = input("Enter Product Name (or 'quit' to finish): ").strip()
        if name.lower() == "quit" or name != "":
            return name
        print("")
        print("Error: Please enter a product name.")
        print("")


def get_quantity():
    while True:
        text = input("Enter Quantity: ").strip()
        if text.isdigit():
            num = int(text)
            if num > 0:
                return num
        print("")
        print("Error: Enter a positive whole number.")
        print("")


def main():
    orders = load_inventory()

    while True:
        display_current_orders(orders)

        product_name = get_product_name()

        if product_name.lower() == "quit":
            save_inventory(orders)
            print("")
            print("All orders saved. Quitting the program.")
            print("")
            break

        quantity = get_quantity()
        new_id = get_next_order_id(orders)

        orders.append([new_id, product_name, quantity])

        print("")
        print("New Order Added:")
        print(new_id + "," + product_name + "," + str(quantity))
        print("Order successfully saved to inventory.txt")
        print("")

        save_inventory(orders)


main()