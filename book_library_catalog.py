import tkinter as tk
from tkinter import ttk

# Book Library Catalog — Python-only Tkinter application
# Run with: python book_library_catalog.py

BOOKS = [
    {"title": "Atomic Habits", "author": "James Clear", "category": "Self Help"},
    {"title": "1984", "author": "George Orwell", "category": "Fiction"},
    {"title": "The Alchemist", "author": "Paulo Coelho", "category": "Fiction"},
    {"title": "Ikigai", "author": "Hector Garcia", "category": "Psychology"},
    {"title": "Harry Potter", "author": "J. K. Rowling", "category": "Fantasy"},
]


class BookLibraryCatalog:
    BG = "#f4f4f4"
    NAVY = "#2c3e50"
    CARD = "#ffffff"
    TEXT = "#222222"
    MUTED = "#64748b"
    BORDER = "#e1e5e9"

    def __init__(self, root):
        self.root = root
        self.root.title("Book Library Catalog")
        self.root.geometry("1050x720")
        self.root.minsize(680, 520)
        self.root.configure(bg=self.BG)

        # Header
        header = tk.Frame(root, bg=self.NAVY, padx=24, pady=24)
        header.pack(fill="x")

        tk.Label(
            header, text="📚  Book Library Catalog",
            bg=self.NAVY, fg="white",
            font=("Arial", 25, "bold")
        ).pack()

        tk.Label(
            header, text="Explore our collection of books",
            bg=self.NAVY, fg="#e5edf5",
            font=("Arial", 12)
        ).pack(pady=(8, 0))

        # Search area
        search_area = tk.Frame(root, bg=self.BG, padx=30, pady=22)
        search_area.pack(fill="x")

        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", self.update_books)

        search_frame = tk.Frame(search_area, bg=self.BG)
        search_frame.pack(fill="x", padx=10)

        self.search_entry = tk.Entry(
            search_frame, textvariable=self.search_var,
            font=("Arial", 12), relief="solid", bd=1,
            bg="white", fg=self.TEXT, insertbackground=self.TEXT
        )
        self.search_entry.pack(fill="x", ipady=10)
        self.search_entry.insert(0, "")
        self.search_entry.configure(
            highlightthickness=1, highlightbackground=self.BORDER,
            highlightcolor="#6b8caf"
        )

        self.result_label = tk.Label(
            search_area, text="", bg=self.BG, fg=self.MUTED,
            font=("Arial", 10)
        )
        self.result_label.pack(anchor="w", padx=10, pady=(8, 0))

        # Scrollable book area
        container = tk.Frame(root, bg=self.BG)
        container.pack(fill="both", expand=True, padx=30, pady=(0, 24))

        self.canvas = tk.Canvas(container, bg=self.BG, highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
        self.cards_frame = tk.Frame(self.canvas, bg=self.BG)

        self.cards_frame.bind(
            "<Configure>",
            lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas_window = self.canvas.create_window(
            (0, 0), window=self.cards_frame, anchor="nw"
        )
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.canvas.bind("<Configure>", self.resize_cards_frame)

        # Mouse wheel scrolling
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

        self.update_books()

    def resize_cards_frame(self, event):
        self.canvas.itemconfigure(self.canvas_window, width=event.width)
        self.render_cards()

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def update_books(self, *_):
        query = self.search_var.get().strip().casefold()
        self.filtered_books = [
            book for book in BOOKS
            if query in book["title"].casefold()
            or query in book["author"].casefold()
            or query in book["category"].casefold()
        ]
        self.result_label.config(
            text=f"{len(self.filtered_books)} book(s) found"
            if query else f"{len(self.filtered_books)} books in the catalog"
        )
        self.render_cards()

    def render_cards(self):
        for widget in self.cards_frame.winfo_children():
            widget.destroy()

        # Responsive two-to-four column layout based on available width
        width = max(self.canvas.winfo_width(), 600)
        columns = max(1, min(4, width // 230))

        for column in range(columns):
            self.cards_frame.grid_columnconfigure(column, weight=1, uniform="cards")

        if not self.filtered_books:
            empty = tk.Frame(self.cards_frame, bg=self.CARD, padx=24, pady=28,
                             highlightbackground=self.BORDER, highlightthickness=1)
            empty.grid(row=0, column=0, sticky="ew", padx=8, pady=8)
            empty.grid_columnconfigure(0, weight=1)
            tk.Label(
                empty, text="No books found",
                font=("Arial", 16, "bold"), bg=self.CARD, fg=self.TEXT
            ).pack()
            tk.Label(
                empty, text="Try another title, author, or category.",
                font=("Arial", 11), bg=self.CARD, fg=self.MUTED
            ).pack(pady=(8, 0))
            return

        for index, book in enumerate(self.filtered_books):
            row, column = divmod(index, columns)
            card = tk.Frame(
                self.cards_frame, bg=self.CARD, padx=20, pady=20,
                highlightbackground=self.BORDER, highlightthickness=1
            )
            card.grid(row=row, column=column, sticky="nsew", padx=8, pady=8)
            card.grid_columnconfigure(0, weight=1)

            tk.Label(
                card, text=book["title"], bg=self.CARD, fg=self.TEXT,
                font=("Arial", 16, "bold"), anchor="w",
                wraplength=220, justify="left"
            ).grid(row=0, column=0, sticky="w", pady=(0, 15))

            tk.Label(
                card, text=f"Author: {book['author']}",
                bg=self.CARD, fg=self.MUTED,
                font=("Arial", 10), anchor="w",
                wraplength=220, justify="left"
            ).grid(row=1, column=0, sticky="w", pady=(0, 10))

            tk.Label(
                card, text=f"Category: {book['category']}",
                bg=self.CARD, fg=self.MUTED,
                font=("Arial", 10), anchor="w",
                wraplength=220, justify="left"
            ).grid(row=2, column=0, sticky="w")

        for column in range(columns):
            self.cards_frame.grid_columnconfigure(column, weight=1)


if __name__ == "__main__":
    root = tk.Tk()
    app = BookLibraryCatalog(root)
    root.mainloop()
