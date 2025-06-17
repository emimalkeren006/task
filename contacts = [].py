contacts = []

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    print("Contact added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for i, c in enumerate(contacts, 1):
            print(f"{i}. {c['name']} - {c['phone']}")

def search_contact():
    query = input("Search by name or phone: ")
    results = [c for c in contacts if query.lower() in c['name'].lower() or query in c['phone']]
    for c in results:
        print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}, Address: {c['address']}")

def update_contact():
    view_contacts()
    try:
        index = int(input("Enter contact number to update: ")) - 1
        contacts[index]['name'] = input("New Name: ")
        contacts[index]['phone'] = input("New Phone: ")
        contacts[index]['email'] = input("New Email: ")
        contacts[index]['address'] = input("New Address: ")
        print("Contact updated.")
    except (IndexError, ValueError):
        print("Invalid input.")

def delete_contact():
    view_contacts()
    try:
        index = int(input("Enter contact number to delete: ")) - 1
        contacts.pop(index)
        print("Contact deleted.")
    except (IndexError, ValueError):
        print("Invalid input.")

def main():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == '1': add_contact()
        elif choice == '2': view_contacts()
        elif choice == '3': search_contact()
        elif choice == '4': update_contact()
        elif choice == '5': delete_contact()
        elif choice == '6': break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()