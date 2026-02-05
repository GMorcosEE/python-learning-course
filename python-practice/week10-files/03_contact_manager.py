# Week 10: Mini Project - Contact Manager with JSON
# Run: python3 week10-files/03_contact_manager.py

import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    
    contacts.append(contact)
    save_contacts(contacts)
    print(f"Added {name} to contacts!")

def view_contacts(contacts):
    if len(contacts) == 0:
        print("No contacts found.")
        return
    
    print("\nAll Contacts:")
    print("=" * 50)
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
        print()

def search_contact(contacts):
    query = input("Enter name to search: ").lower()
    found = False
    
    for contact in contacts:
        if query in contact['name'].lower():
            print(f"\nFound: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            found = True
    
    if not found:
        print("No contacts found.")

def delete_contact(contacts):
    name = input("Enter name to delete: ")
    
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name.lower():
            contacts.pop(i)
            save_contacts(contacts)
            print(f"Deleted {name} from contacts!")
            return
    
    print("Contact not found.")

def main():
    contacts = load_contacts()
    
    print("Contact Manager")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Quit")
        
        choice = input("\nChoose an option (1-5): ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5")

main()

# TODO: Add a feature to edit existing contacts
# TODO: Add a feature to export contacts to CSV
# TODO: Add a feature to count total contacts
