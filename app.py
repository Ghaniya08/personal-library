# "Use This Code For Terminal"

# import pandas as pd
# print("Wellcome to the Personal Library App")

# def menu():
#     print("1. Add a book")
#     print("2. Remove a book")
#     print("3. Search for a book")
#     print("4. Display all books")
#     print("5. Display statistics")
#     print("6.Exit")

# all_books: list = []

# def add_book():
#     title = input("Enter Your Book Title: ")
#     author = input(f"Enter Your Book Author: ")
#     publication_year = input("Enter Your Book Publication Year: ")
#     genre = input("Enter Your Book Genre: ")
#     read_book = input("Have you read this book? (yes/no): ")
#     book = {
#     "title" : title,
#     "author" : author,
#     "publication-year": publication_year,
#     "genre" : genre,
#     "read" : read_book
#     }
#     all_books.append(book)
#     print("\nBook added successfully!\n")
#     print("\nYour Book List:")
#     for book in all_books:
#         print(book)


# def remove_book():
#     book_name = input("Enter the name of the book you want to remove: ")
#     for book in all_books:
#         if book["title"].lower() == book_name.lower():
#             all_books.remove(book)
#             print(f"\n'{book_name}' has been removed from your library.\n")
#             return
#     print(f"\n'{book_name}' is not in your library.\n")

# def search_book():
#     book_name = input("Enter the name of the book you want to search: ")
#     for book in all_books:
#         if book["title"].lower() == book_name.lower():
#             print("Book Found")
#             print(f"Title : {book['title']}")
#             print(f"Author : {book['author']}")
#             print(f"Publication Year : {book['publication-year']}")
#             print(f"Genre : {book['genre']}")
#             print(f"Read : {book['read']}")
#             return
#     print(f"\n'{book_name}' is not found in your library.\n")
  
# def display_all_books():
#     if not all_books:
#         print("\nYour library is empty.\n")
#     else:
#         df = pd.DataFrame(all_books)
#         print("\nYour Book List:")
#         print(df.to_string(index=False))

# def display_statistics():
#     if not all_books:
#         print("\nNo statistics available. Your library is empty.\n")
#         return

#     total_books = len(all_books)
#     read_books = sum(1 for book in all_books if book["read"].lower() == "yes")
#     unread_books = total_books - read_books
#     read_percentage = (read_books / total_books) * 100

#     print("\n📊 Library Statistics:")
#     print(f"Total books       : {total_books}")
#     print(f"Books read        : {read_books}")
#     print(f"Books not read    : {unread_books}")
#     print(f"Percentage read   : {read_percentage:.1f}%")


# while True:
#     menu()
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         print("Add a book")
#         add_book()
#     elif choice == "2":
#         print("Remove a book")
#         remove_book()      
#     elif choice == "3":
#         print("Search for a book")
#         search_book()
#     elif choice == "4":
#         print("Display all books")
#         display_all_books()
#     elif choice == "5":
#         print("Display statistics")
#         display_statistics()
#     elif choice == "6":
#         print("Exit")   
#         break
#     else:
#         print("Invalid choice. Please try again.")

# Use this code for For Streamlit

import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Personal Library",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Personal Library App")

if "all_books" not in st.session_state:
    st.session_state.all_books = []

menu = st.sidebar.radio("Menu", [
    "Add a Book",
    "Remove a Book",
    "Search for a Book",
    "Display All Books",
    "Display Statistics"
])

if menu == "Add a Book":
    st.subheader("➕ Add a New Book")
    with st.form("add_form"):
        title = st.text_input("Book Title")
        author = st.text_input("Author")
        year = st.text_input("Publication Year")
        genre = st.text_input("Genre")
        read = st.selectbox("Have you read this book?", ["yes", "no"])
        submitted = st.form_submit_button("Add Book")

        if submitted:
            book = {
                "title": title,
                "author": author,
                "publication-year": year,
                "genre": genre,
                "read": read
            }
            st.session_state.all_books.append(book)
            st.success("Book added successfully!")

elif menu == "Remove a Book":
    st.subheader("🗑️ Remove a Book")
    if not st.session_state.all_books:
        st.info("No books to remove.")
    else:
        titles = [book["title"] for book in st.session_state.all_books]
        book_to_remove = st.selectbox("Select a book to remove", titles)
        if st.button("Remove Book"):
            st.session_state.all_books = [book for book in st.session_state.all_books if book["title"] != book_to_remove]
            st.success(f"'{book_to_remove}' has been removed.")

elif menu == "Search for a Book":
    st.subheader("🔍 Search for a Book")
    search_title = st.text_input("Enter book title to search")
    if st.button("Search"):
        found = False
        for book in st.session_state.all_books:
            if book["title"].lower() == search_title.lower():
                st.success("Book Found:")
                st.write(book)
                found = True
                break
        if not found:
            st.error("Book not found in your library.")

elif menu == "Display All Books":
    st.subheader("📖 Your Book List")
    if not st.session_state.all_books:
        st.info("Your library is empty.")
    else:
        df = pd.DataFrame(st.session_state.all_books)
        st.dataframe(df, use_container_width=True)

elif menu == "Display Statistics":
    st.subheader("📊 Library Statistics")
    if not st.session_state.all_books:
        st.info("No statistics available. Your library is empty.")
    else:
        total = len(st.session_state.all_books)
        read = sum(1 for b in st.session_state.all_books if b["read"].lower() == "yes")
        unread = total - read
        percentage = (read / total) * 100

        st.metric("Total Books", total)
        st.metric("Books Read", read)
        st.metric("Books Unread", unread)
        st.metric("% Read", f"{percentage:.1f}%")

st.markdown("""
<div class="footer">
    <p>Personal Library App <a href="https://github.com/Ghaniya08">Made By Ghaniya Khan</a> </p>
</div>
""", unsafe_allow_html=True)