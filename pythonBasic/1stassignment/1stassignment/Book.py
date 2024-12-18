books = ["Book1", "Book2", "Book3"]
while True:
    print("1. View available books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Available books:", books)
    elif choice == 2:
        book = input("Enter the book to borrow: ")
        if book in books:
            books.remove(book)
            print("You borrowed", book)
        else:
            print("Book not available")
    elif choice == 3:
        book = input("Enter the book to return: ")
        books.append(book)
        print("You returned", book)
    elif choice == 4:
        break
    else:
        print("Invalid choice")
