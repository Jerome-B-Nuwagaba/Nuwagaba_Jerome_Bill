inventory = {
    "001": {"name": "Flour", "price": 20000},
    "002": {"name": "Eggs", "price": 16000},
    "003": {"name": "Milk", "price": 18000}
}

def display_inventory():    
    print("\nCurrent Inventory:")    
    print(f"{'ID':<10}{'Name':<15}{'Price':<10}")    
    for item_id, details in inventory.items():
        print(f"{item_id:<10}{details['name']:<15}shs.{details['price']:<10}")
    

def add_item():   
    print("\nAdd New Item")
    item_id = input("Enter item ID (e.g., 004): ")
    name = input("Enter item name: ")
    price = int(input("Enter item price: "))    
    inventory[item_id] = {"name": name, "price": price}
    print(f"\n{name} added to inventory successfully!")

def update_item():    
    display_inventory()
    item_id = input("\nEnter item ID to update: ")
    
    if item_id in inventory:
        print(f"\nCurrent details for {inventory[item_id]['name']}:")
        print(f"Price: {inventory[item_id]['price']}")        
        
        
        print("\nWhat would you like to update?")
        print("1. Name?")
        print("2. Price?")
        choice = input("Enter choice (1-2): ")
        
        if choice == "1":
            new_name = (input("Enter new name: "))
            inventory[item_id]["name"] = new_name
            print(f"Name updated to {new_name}")
        elif choice == "2":
            new_price = int(input("Enter new price: "))
            inventory[item_id]["price"] = new_price
            print(f"Price updated to shs.{new_price}")
        else:
            print("Invalid choice")
    else:
        print("Item ID not found in inventory")

def main_menu():    
    while True:
        print("\nInventory Management System")
        print("1. View Inventory")
        print("2. Add New Item")
        print("3. Update Item")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            display_inventory()
        elif choice == "2":
            add_item()
        elif choice == "3":
            update_item()
        elif choice == "4":
            print("Exited!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()