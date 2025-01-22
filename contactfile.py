import pickle

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email}, Address: {self.address}"

class ContactManager:
    def __init__(self):
        self.contacts = self.load_contacts()

    # Load contacts from file (if exists)
    def load_contacts(self):
        try:
            with open("contacts.pkl", "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return []

    # Save contacts to file
    def save_contacts(self):
        with open("contacts.pkl", "wb") as file:
            pickle.dump(self.contacts, file)

    # Add a new contact
    def add_contact(self, name, phone_number, email, address):
        new_contact = Contact(name, phone_number, email, address)
        self.contacts.append(new_contact)
        self.save_contacts()
        print(f"Contact '{name}' added successfully!")

    # View all contacts
    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for idx, contact in enumerate(self.contacts, 1):
                print(f"{idx}. {contact}")

    # Search contact by name or phone number
    def search_contact(self, search_term):
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                print(contact)
                found = True
        if not found:
            print(f"No contact found for '{search_term}'.")

    # Update a contact's details
    def update_contact(self, index, name=None, phone_number=None, email=None, address=None):
        if 0 < index <= len(self.contacts):
            contact = self.contacts[index - 1]
            if name:
                contact.name = name
            if phone_number:
                contact.phone_number = phone_number
            if email:
                contact.email = email
            if address:
                contact.address = address
            self.save_contacts()
            print(f"Contact '{contact.name}' updated successfully!")
        else:
            print("Invalid contact index.")

    # Delete a contact
    def delete_contact(self, index):
        if 0 < index <= len(self.contacts):
            deleted_contact = self.contacts.pop(index - 1)
            self.save_contacts()
            print(f"Contact '{deleted_contact.name}' deleted successfully!")
        else:
            print("Invalid contact index.")

def show_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    manager = ContactManager()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(name, phone_number, email, address)

        elif choice == "2":
            manager.view_contacts()

        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            manager.search_contact(search_term)

        elif choice == "4":
            index = int(input("Enter the contact index to update: "))
            name = input("Enter new name (leave blank to keep current): ")
            phone_number = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            manager.update_contact(index, name, phone_number, email, address)

        elif choice == "5":
            index = int(input("Enter the contact index to delete: "))
            manager.delete_contact(index)

        elif choice == "6":
            print("Exiting the Contact Management System.")
            break

        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
