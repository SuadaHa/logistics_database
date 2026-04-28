from db_setup import create_database
import tkinter as tk
from tkinter import messagebox
import os

print("RUNNING FILE:", os.path.abspath(__file__))
print(os.path.abspath("app.db"))


def add_book():
    window = tk.Toplevel()
    window.title("Add Book")
    window.geometry("400x300")

    tk.Label(window, text="Book Title").pack(pady=5)
    title_entry = tk.Entry(window, width=30)
    title_entry.pack()

    tk.Label(window, text="Author").pack(pady=5)
    author_entry = tk.Entry(window, width=30)
    author_entry.pack()

    tk.Label(window, text="ISBN").pack(pady=5)
    isbn_entry = tk.Entry(window, width=30)
    isbn_entry.pack()

    def save_book():
        title = title_entry.get()
        author = author_entry.get()
        isbn = isbn_entry.get()

        messagebox.showinfo(
            "Book Saved",
            f"Title: {title}\nAuthor: {author}\nISBN: {isbn}"
        )

    tk.Button(window, text="Save Book", command=save_book).pack(pady=20)


def add_member():
    window = tk.Toplevel()
    window.title("Add Member")
    window.geometry("400x300")

    tk.Label(window, text="Member Name").pack(pady=5)
    name_entry = tk.Entry(window, width=30)
    name_entry.pack()

    tk.Label(window, text="Email").pack(pady=5)
    email_entry = tk.Entry(window, width=30)
    email_entry.pack()

    def save_member():
        name = name_entry.get()
        email = email_entry.get()

        messagebox.showinfo(
            "Member Saved",
            f"Name: {name}\nEmail: {email}"
        )

    tk.Button(window, text="Save Member", command=save_member).pack(pady=20)


def view_books():
    messagebox.showinfo("View Books", "This will show all books")


def issue_book():
    messagebox.showinfo("Issue Book", "This will issue a book")


def return_book():
    messagebox.showinfo("Return Book", "This will return a book")


def main():
    print("Starting application...")

    create_database()

    print("Creating window")

    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("520x360")

    title = tk.Label(
        root,
        text="Welcome to the Library Management System",
        font=("Arial", 18)
    )
    title.pack(pady=20)

    tk.Button(root, text="Add Book", width=20, command=add_book).pack(pady=10)
    tk.Button(root, text="View Books", width=20, command=view_books).pack(pady=10)
    tk.Button(root, text="Add Member", width=20, command=add_member).pack(pady=10)
    tk.Button(root, text="Issue Book", width=20, command=issue_book).pack(pady=10)
    tk.Button(root, text="Return Book", width=20, command=return_book).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
