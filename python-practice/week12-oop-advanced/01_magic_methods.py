# Week 12: Advanced OOP - Magic Methods
# Run: python3 week12-oop-advanced/01_magic_methods.py

# Magic methods (also called dunder methods) start and end with double underscores
# They allow you to define how objects behave with built-in Python operations

class Book:
    """Book class with magic methods"""
    
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
    
    # __str__ - defines how object is printed
    def __str__(self) -> str:
        return f"'{self.title}' by {self.author}"
    
    # __repr__ - defines official string representation (for debugging)
    def __repr__(self) -> str:
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    # __len__ - defines behavior for len() function
    def __len__(self) -> int:
        return self.pages
    
    # __eq__ - defines behavior for == operator
    def __eq__(self, other) -> bool:
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False
    
    # __lt__ - defines behavior for < operator (less than)
    def __lt__(self, other) -> bool:
        if isinstance(other, Book):
            return self.pages < other.pages
        return NotImplemented
    
    # __add__ - defines behavior for + operator
    def __add__(self, other):
        if isinstance(other, Book):
            combined_title = f"{self.title} & {other.title}"
            combined_author = f"{self.author} & {other.author}"
            combined_pages = self.pages + other.pages
            return Book(combined_title, combined_author, combined_pages)
        return NotImplemented


# Using magic methods
book1 = Book("Python Basics", "John Doe", 300)
book2 = Book("Advanced Python", "Jane Smith", 450)
book3 = Book("Python Basics", "John Doe", 300)

# __str__ is used by print()
print(book1)
print(book2)

# __repr__ is used in interactive mode or with repr()
print(f"\nRepr: {repr(book1)}")

# __len__ is used by len()
print(f"\nBook 1 has {len(book1)} pages")
print(f"Book 2 has {len(book2)} pages")

# __eq__ is used by ==
print(f"\nbook1 == book2: {book1 == book2}")
print(f"book1 == book3: {book1 == book3}")

# __lt__ is used by <
print(f"\nbook1 < book2: {book1 < book2}")

# Sorting uses __lt__
books = [book2, book1, book3]
sorted_books = sorted(books)
print("\nBooks sorted by pages:")
for book in sorted_books:
    print(f"  {book} - {len(book)} pages")

# __add__ is used by +
combined = book1 + book2
print(f"\nCombined book: {combined}")
print(f"Total pages: {len(combined)}")


# More magic methods example
class Vector:
    """2D vector with mathematical operations"""
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        """Vector addition"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        """Vector subtraction"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, scalar: float):
        """Scalar multiplication"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other) -> bool:
        """Vector equality"""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
    
    def __abs__(self) -> float:
        """Vector magnitude"""
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __getitem__(self, index: int) -> float:
        """Allow indexing: v[0] for x, v[1] for y"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")


# Using Vector class
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"\n--- Vector Operations ---")
print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"v1 * 2: {v1 * 2}")
print(f"|v1|: {abs(v1):.2f}")
print(f"v1[0]: {v1[0]}, v1[1]: {v1[1]}")


# Context manager magic methods
class FileManager:
    """Custom context manager for file operations"""
    
    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Called when entering 'with' block"""
        print(f"Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block"""
        if self.file:
            print(f"Closing {self.filename}")
            self.file.close()
        return False


# Using context manager
print("\n--- Context Manager ---")
with FileManager("test.txt", "w") as f:
    f.write("Hello from custom context manager!")

with FileManager("test.txt", "r") as f:
    content = f.read()
    print(f"Content: {content}")


# TODO: Create a Money class with __add__, __sub__, and __str__ methods
# TODO: Create a Temperature class that can be compared with <, >, ==
# TODO: Add __mul__ and __truediv__ to the Vector class
# TODO: Create a custom iterator class with __iter__ and __next__
