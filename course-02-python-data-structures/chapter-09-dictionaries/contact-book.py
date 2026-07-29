# Contact Book
contacts = {}


# Show the menu options
print("Welcome to the Contact Book!\n")

print("1 - Add a new contact")
print("2 - Search a contact")
print("3 - Show all contacts")
print("4 - Delete a contact")   
print("5 - Exit\n")

option = int(input("Choose an option: "))

# Main loop
while option != 5:
    if option == 1:
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        contacts[name] = phone
        print(f"Contact {name} added successfully!\n")
    
    elif option == 2:
        name = input("Enter contact name to search: ").strip()
        phone = contacts.get(name)
        if phone is not None:
            print(f"{name}: {phone}\n")
        else:
            print(f"Contact {name} not found.\n")
    
    elif option == 3:
        if contacts:
            print("Contacts:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
            print()
        else:
            print("No contacts found.\n")
    
    elif option == 4:
        name = input("Enter contact name to delete: ").strip()
        phone = contacts.get(name)
        if phone is not None:
            del contacts[name]
            print(f"Contact {name} deleted successfully!\n")
        else:
            print(f"Contact {name} not found.\n")
    elif option == 5:
        print("Exiting the Contact Book. Goodbye!")
        break
    
    else:
        print("Invalid option. Please try again.\n")

    # Show the menu options again
    print("Welcome to the Contact Book!\n")

    print("1 - Add a new contact")
    print("2 - Search a contact")
    print("3 - Show all contacts")
    print("4 - Delete a contact")   
    print("5 - Exit\n")

    # Get the next option from the user
    option = int(input("Choose an option: "))