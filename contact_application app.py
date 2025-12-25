import json

def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Save Contacts")
    print("7. Load Contacts")
    print("8. Exit")

def save_to_file(contact_book):
    with open("data.json", "w") as f:
        json.dump(contact_book, f, indent=4)

def load_from_file():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def add_contact(contact_book):
    name = input("Name: ")
    if name in contact_book:
        print("Contact already exists!")
        return
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contact_book[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print("Contact added successfully!")

def view_contact(contact_book):
    name = input("Name: ")
    if name in contact_book:
        c = contact_book[name]
        print(f"Phone: {c['phone']}")
        print(f"Email: {c['email']}")
        print(f"Address: {c['address']}")
    else:
        print("Contact not found!")

def edit_contact(contact_book):
    name = input("Name: ")
    if name not in contact_book:
        print("Contact not found!")
        return

    c = contact_book[name]
    phone = input(f"Phone ({c['phone']}): ") or c["phone"]
    email = input(f"Email ({c['email']}): ") or c["email"]
    address = input(f"Address ({c['address']}): ") or c["address"]

    contact_book[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print("Contact updated successfully!")

def delete_contact(contact_book):
    name = input("Name: ")
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def list_all_contacts(contact_book):
    if not contact_book:
        print("No contacts available.")
        return

    for name, c in contact_book.items():
        print("-" * 20)
        print(f"Name: {name}")
        print(f"Phone: {c['phone']}")
        print(f"Email: {c['email']}")
        print(f"Address: {c['address']}")

contact_book = load_from_file()

while True:
    display_menu()
    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        add_contact(contact_book)
    elif choice == "2":
        view_contact(contact_book)
    elif choice == "3":
        edit_contact(contact_book)
    elif choice == "4":
        delete_contact(contact_book)
    elif choice == "5":
        list_all_contacts(contact_book)
    elif choice == "6":
        save_to_file(contact_book)
        print("Contacts saved successfully!")
    elif choice == "7":
        contact_book = load_from_file()
        print("Contacts loaded successfully!")
    elif choice == "8":
        save_to_file(contact_book)
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice!")
