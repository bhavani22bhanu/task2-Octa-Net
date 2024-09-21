import datetime

# Global constants
TAX_RATE = 0.05  # 5% tax rate
DISCOUNT_THRESHOLD = 100  # Discount applies if the subtotal exceeds $100
DISCOUNT_RATE = 0.10  # 10% discount

# Receipt information
items = []

def add_item():
    """Accepts input for item name, price, and quantity and adds it to the list of items."""
    name = input("Enter the item name: ")
    price = float(input("Enter the price of the item: $"))
    quantity = int(input("Enter the quantity: "))
    
    item = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "total_price": price * quantity
    }
    items.append(item)
    print(f"Added {quantity} {name}(s) to the cart.")

def calculate_totals():
    """Calculates the subtotal, tax, discount, and final total."""
    subtotal = sum(item['total_price'] for item in items)
    tax = subtotal * TAX_RATE
    discount = 0
    if subtotal > DISCOUNT_THRESHOLD:
        discount = subtotal * DISCOUNT_RATE
    final_total = subtotal + tax - discount
    return subtotal, tax, discount, final_total

def generate_receipt():
    """Generates and displays a detailed receipt."""
    print("\n--- Receipt ---")
    print(f"Date: {datetime.datetime.now()}")
    print("----------------------------")
    
    for item in items:
        print(f"{item['quantity']}x {item['name']} @ ${item['price']:.2f} each = ${item['total_price']:.2f}")
    
    subtotal, tax, discount, final_total = calculate_totals()
    print("----------------------------")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax (5%): ${tax:.2f}")
    print(f"Discount: -${discount:.2f}")
    print(f"Total: ${final_total:.2f}")
    print("----------------------------")
    
    # Save the receipt to a text file
    save_receipt_to_file(subtotal, tax, discount, final_total)

def save_receipt_to_file(subtotal, tax, discount, final_total):
    """Saves the receipt as a text file."""
    filename = f"receipt_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as file:
        file.write(f"--- Receipt ---\n")
        file.write(f"Date: {datetime.datetime.now()}\n")
        file.write("----------------------------\n")
        for item in items:
            file.write(f"{item['quantity']}x {item['name']} @ ${item['price']:.2f} each = ${item['total_price']:.2f}\n")
        file.write("----------------------------\n")
        file.write(f"Subtotal: ${subtotal:.2f}\n")
        file.write(f"Tax (5%): ${tax:.2f}\n")
        file.write(f"Discount: -${discount:.2f}\n")
        file.write(f"Total: ${final_total:.2f}\n")
        file.write("----------------------------\n")
    print(f"\nReceipt saved as {filename}")

def shopping_cart():
    """Main function to handle the shopping cart operations."""
    while True:
        print("\nShopping Cart Menu:")
        print("1. Add item to cart")
        print("2. View and generate receipt")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            add_item()
        elif choice == '2':
            if items:
                generate_receipt()
            else:
                print("No items in the cart.")
        elif choice == '3':
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the shopping cart
shopping_cart()
