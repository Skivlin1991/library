library = {
    "name": "CodeClan Library",
    "books": [
        {
            "author": "George RR Martin",
            "title": "A Song of Ice and Fire"
        },
        {
            "author": "J R. R. Tolkien",
            "title": "The Hobbit"
        },
        {
            "author": "Paul Barry",
            "title": "Head-First Python"
        },
        {
            "author": "Allen B. Downey",
            "title": "Think Python: How to Think Like a Computer Scientist"
        },
        {
            "author": "Eric Matthes",
            "title": "Python Crash Course"
        }
    ]
}

library_name = library['name']
print(f"welcome to {library_name}")

option = ""
while option != "q":
    print("Options:")
    print("1 - List all books")
    print("2 - Search for a book by title")
    print("3 - Add a book")
    print("4 - Remove a book")
    print("5 - Update a book")
    print("q - Quit")
    option = input("What would you like to do? \n")

    if option == "1":
        print("Listing all books...")
        for books in library ["books"]:
            title = books ['title']
            author = books ['author']
            print (f'{title} by {author}')
        # TODO - List all books

    if option == "2":
        print("Searching for a book by title...")
        for books in library['books']:
            if books['title'].lower() == title.lower():
                found_books = books
            if found_books != None:
                title = found_books['title']
                author = found_books['author']
                print(f'found{title} by {author} ')
            else:
                print(f"{title} not here hahaah ")
        # TODO - Search for a book by title

    if option == "3":
        print("Adding a book...")
        title = input ("new title:")
        author = input ("new author:")
        newbook = {"title": title, 'author':author}
        library["books"].append(newbook)
        # TODO - Remove a book
        # TODO - Add a book

    if option == "4":
        print("Removing a book...")
        title_to_delete = input ("enter title")
        book_to_delete = None
    for books in library['books']:
        if books['title'].lower() == title_to_delete.lower():
            book_to_delete = books  
        if book_to_delete != None:
            library['books'].remove()(book_to_delete)
        else :
            print(f"{title_to_delete}not found haha")
        # TODO - Remove a book

    if option == "5":
        print("Updating a book...")
        title_to_update = input ('enter title:')
        books_to_update = None
        for books in library['books']:
            if books['title'].lower() == title_to_update.lower():
                books_to_update = books
            if books_to_update!=None:
                library['books'].update()(books_to_update)
            else :
                print(f"{title_to_update}not found haha")
            
        # TODO - Update a book