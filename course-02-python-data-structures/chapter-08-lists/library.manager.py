# Library Manager

books = []

print("Welcome to the Library Manager! \n")

# Start the main loop
while True:
    print("1 - Add a book")
    print("2 - View all books")
    print("3 - Search for a book")
    print("4 - Remove a book")
    print("5 - Exit \n")

    # Ask the user to select an option
    option = int(input("Please select an option: "))

    if option == 1:
        book = input("Enter the name of the book: ")
        books.append(book)
        print(f"{book} has been added to the library.")

    elif option == 2:
        print("Books in the library:")
        for book in books:
            print(book)

    elif option == 3:
        search = input("Enter the name of the book to search for: ")
        if search in books:
            print(f"{search} is available in the library.")
        else:
            print(f"{search} is not available in the library.")

    elif option == 4:
        remove_book = input("Enter the name of the book to remove: ")
        if remove_book in books:
            books.remove(remove_book)
            print(f"{remove_book} has been removed from the library.")
        else:
            print(f"{remove_book} is not in the library.")

    elif option == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")