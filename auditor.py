total_inventory = 0
failed_entries = 0

while True:
    entry = input("Enter stock quantity (or 'quit' to finish): ")

    if entry == "quit":
        break

    if not entry.isdigit():
        print("Error: Please enter a valid whole number.")
        failed_entries += 1
        continue

    quantity = int(entry)

    if quantity < 0:
        print("Error: Negative values are not allowed.")
        failed_entries += 1
        continue

    total_inventory += quantity
    print(f"Accepted. Running total: {total_inventory}")

    if total_inventory > 500:
        print("ALERT: Overstock! Inventory has exceeded 500 units.")
        break

print("\n--- Final Report ---")
print(f"Total Units Processed: {total_inventory}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")