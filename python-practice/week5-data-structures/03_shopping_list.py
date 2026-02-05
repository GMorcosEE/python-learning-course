# Week 5: Mini Project - Shopping List Manager
# Run: python3 week5-data-structures/03_shopping_list.py

shopping_list = []

print("Shopping List Manager")
print("=" * 30)

while True:
    print("\nOptions:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Clear list")
    print("5. Quit")
    
    choice = input("\nChoose an option (1-5): ")
    
    if choice == "1":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"Added '{item}' to the list")
    
    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"Removed '{item}' from the list")
        else:
            print(f"'{item}' not found in the list")
    
    elif choice == "3":
        if len(shopping_list) == 0:
            print("Your list is empty")
        else:
            print("\nYour Shopping List:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
    
    elif choice == "4":
        shopping_list.clear()
        print("List cleared")
    
    elif choice == "5":
        print("Goodbye!")
        break
    
    else:
        print("Invalid option. Please choose 1-5")

# TODO: Add a feature to show the number of items in the list
# TODO: Add a feature to check if a specific item is in the list
# TODO: Add a feature to sort the list alphabetically
