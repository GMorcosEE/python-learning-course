# Week 6: Mini Project - Simple Phonebook
# Run: python3 week6-data-structures/03_phonebook.py

phonebook = {}

print("Simple Phonebook")
print("=" * 30)

while True:
    print("\nOptions:")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. List all contacts")
    print("5. Quit")
    
    choice = input("\nChoose an option (1-5): ")
    
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        phonebook[name] = phone
        print(f"Added {name} to phonebook")
    
    elif choice == "2":
        name = input("Enter name to search: ")
        if name in phonebook:
            print(f"{name}: {phonebook[name]}")
        else:
            print(f"{name} not found in phonebook")
    
    elif choice == "3":
        name = input("Enter name to delete: ")
        if name in phonebook:
            del phonebook[name]
            print(f"Deleted {name} from phonebook")
        else:
            print(f"{name} not found in phonebook")
    
    elif choice == "4":
        if len(phonebook) == 0:
            print("Phonebook is empty")
        else:
            print("\nAll Contacts:")
            for name, phone in phonebook.items():
                print(f"{name}: {phone}")
    
    elif choice == "5":
        print("Goodbye!")
        break
    
    else:
        print("Invalid option. Please choose 1-5")

# TODO: Add email addresses to contacts (make each contact a dictionary)
# TODO: Add a feature to update a contact's phone number
# TODO: Sort contacts alphabetically when listing them
