def get_valid_input():
    while True:
        entry = input("Enter stock quantity (or 'quit' to finish): ")
        
        if entry.lower() == "quit":
            return "quit" ## returns quit to break
        
        if not entry.isdigit():
            print("Error: Please enter a valid whole number.")
            return "invalid" ## returns invalid for failed attempts increment
        
        return int(entry) ## returns stock quantity 

    
def process_delivery(current_total, new_value):
    current_total += new_value
    return current_total

def calculate_tax(amount):
    tax = amount * 0.1
    return tax 

def generate_report(total_units, failed_attempts):
    print("\n--- Final Report ---")
    print(f"Total Deliveries Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


def main():
    total_inventory = 0
    deliveries_processed = 0
    failed_attempts = 0

    while True:
        quantity = get_valid_input()

        if quantity == "quit":
            break
        elif quantity == "invalid":
            failed_attempts += 1
            continue

        total_inventory = process_delivery(total_inventory, quantity)
        tax = calculate_tax(quantity)
        deliveries_processed += 1

        print(f"Added {quantity} unit of stock(s), tax on this delivery is ${tax:.2f}")

    generate_report(deliveries_processed, failed_attempts)

main()