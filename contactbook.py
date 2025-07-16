contacts = []

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Name: ").strip()
    phone = input("Phone Number: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("✅ Contact added successfully!")

def view_contacts():
    if not contacts:
        print("\n📭 No contacts found.")
        return
    print("\n--- Contact List ---")
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    keyword = input("\n🔍 Enter name or phone number to search: ").strip().lower()
    found = False
    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            print("\n✅ Contact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
            break
    if not found:
        print("❌ No contact matched your search.")

def update_contact():
    name = input("\n✏️ Enter the name of the contact to update: ").strip().lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            print("Leave any field blank to keep it unchanged.")
            new_phone = input("New Phone Number: ").strip()
            new_email = input("New Email: ").strip()
            new_address = input("New Address: ").strip()
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            if new_address:
                contact['address'] = new_address
            print("✅ Contact updated successfully!")
            return
    print("❌ Contact not found.")

def delete_contact():
    name = input("\n🗑️ Enter the name of the contact to delete: ").strip().lower()
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name:
            contacts.pop(i)
            print("🗑️ Contact deleted successfully!")
            return
    print("❌ Contact not found.")

def show_menu():
    print("\n=== Contact Book Menu ===")
    print("1. 📥 Add Contact")
    print("2. 📇 View Contact List")
    print("3. 🔍 Search Contact")
    print("4. ✏️ Update Contact")
    print("5. 🗑️ Delete Contact")
    print("6. 🚪 Exit")

def main():
    print("👋 Welcome to the Python Contact Book")
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
