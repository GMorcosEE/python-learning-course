# Week 9: Mini Project - Simple Note Taking App
# Run: python3 week9-files/03_note_taking_app.py

import os

NOTES_FILE = "notes.txt"

def create_notes_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as file:
            file.write("")

def add_note():
    note = input("Enter your note: ")
    with open(NOTES_FILE, "a") as file:
        file.write(note + "\n")
    print("Note added!")

def view_notes():
    if not os.path.exists(NOTES_FILE):
        print("No notes found.")
        return
    
    with open(NOTES_FILE, "r") as file:
        notes = file.readlines()
    
    if len(notes) == 0:
        print("No notes found.")
    else:
        print("\nYour Notes:")
        print("=" * 40)
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note.strip()}")

def clear_notes():
    confirm = input("Are you sure you want to clear all notes? (yes/no): ")
    if confirm.lower() == "yes":
        with open(NOTES_FILE, "w") as file:
            file.write("")
        print("All notes cleared!")
    else:
        print("Cancelled.")

def count_notes():
    if not os.path.exists(NOTES_FILE):
        print("No notes found.")
        return
    
    with open(NOTES_FILE, "r") as file:
        notes = file.readlines()
    
    print(f"You have {len(notes)} note(s).")

def main():
    create_notes_file()
    
    print("Simple Note Taking App")
    print("=" * 40)
    
    while True:
        print("\nOptions:")
        print("1. Add note")
        print("2. View notes")
        print("3. Count notes")
        print("4. Clear all notes")
        print("5. Quit")
        
        choice = input("\nChoose an option (1-5): ")
        
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            count_notes()
        elif choice == "4":
            clear_notes()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5")

main()

# TODO: Add a feature to delete a specific note by number
# TODO: Add a feature to search notes for a keyword
# TODO: Add timestamps to each note
