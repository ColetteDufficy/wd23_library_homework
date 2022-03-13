library = {
    "name": "CodeClan Library",
    "books": [
        {"author": "George RR Martin","title": "A Song of Ice and Fire"},
        {"author": "J R. R. Tolkien","title": "The Hobbit"},
        {"author": "Paul Barry","title": "Head-First Python"},
        {"author": "Allen B. Downey","title": "Think Python: How to Think Like a Computer Scientist"},
        {"author": "Eric Matthes","title": "Python Crash Course"}
    ]
}

# TODO - Print welcome statement including library name
print(f'Welcome to the {library["name"]}.')
            

option = "" # empty quote marks essentially equate to 'null'
while option != "q":
    print("Choose an option:")
    print("1 - List all books")
    print("2 - Search for a book by title")
    print("3 - Add a book")
    print("4 - Remove a book")
    print("5 - Update a book")
    print("q - Quit")
    print()
    option = input("What would you like to do? \n")


# TODO - List all books
    if option == "1":
        print('The following books are in stock:' )
        books = library["books"]
        for book in books:
            print(f'Author: {book["author"]} Title: {book["title"]}')     
    print()


#  # TODO - Search for a book by title
#     if option == "9":
#         print("Searching for a book by title...")
#         books = library["books"]
#         book_title = input("Enter a keyword from the title: ")
#         for book in books:
#             if book_title.lower() == "a song":
#                 print('Great choice, "A Song of Ice and Fire" is in stock')
#                 break
#             elif book_title.lower() == "the hobbit":
#                 print('Great choice, "The Hobbit" is in stock')
#                 break
#             elif book_title.lower() == "head":
#                 print('Great choice, "Head-First Python" is in stock')
#                 break
#             elif book_title.lower() == "think":
#                 print('Great choice, "Think Python: How to Think Like a Computer Scientist" is in stock.')
#                 break
#             elif book_title.lower() == "python":
#                 print('Great choice, "Python Crash Course" is in stock.')
#                 break
#             else:
#                 print("Sorry, that title is not in stock")
#                 break
#     print()
    

# TODO - Search for a book by title (tried List Comprehension) this does what the code above does... more efficiently
    if option == "2":
        print("Searching for a book by title...")
        books = library["books"]
        book_title = input("Enter the title here: ")
        books = [book for book in books if book['title'].lower() == book_title.lower()]
        if len(books) == 0:
            print("Sorry, that title is not in stock.")
        else:
            print(f'Author: {books[0]["author"]} Title: {books[0]["title"]}')
        print()
                       

# TODO - User add a book
    if option == "3":
        print("Adding a book...")
        temp_books = library["books"]
        temp_books.append({'author':input("Enter author name here: "), 'title':input("Enter new title here: ")})
        for book in temp_books:
            print(f'Author: {book["author"]} Title: {book["title"]}')
        print()
            

# TODO - Remove a book
    if option == "4":
        print("Removing a book...")
        books = library["books"]
        book_to_delete = input("What book do you want to remove? ")
        books = [book for book in books if book['title'].lower() != book_to_delete.lower() ]
        print(books)
        print()
            

# TODO - Update a book
    if option == "5":
        print("Updating a book...")
        books = library["books"]
        book_to_update = input("What book do you want to update? ")
        for book in books:
            if book['title'].lower() == book_to_update.lower():
                book.update({'author':input("Enter author name here: "), 'title': input("Enter new title here: ")})
                break
        print(books)