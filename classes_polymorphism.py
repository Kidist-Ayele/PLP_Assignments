
# ========================================
# PART 1: DESIGN YOUR OWN CLASS
# ========================================

class Book:
    """A simple book class"""
    
    def __init__(self, title, author, pages):
        """Constructor - creates a new book"""
        self.title = title      # Book title
        self.author = author    # Book author
        self.pages = pages      # Number of pages
        self.is_borrowed = False
    
    def borrow(self):
        """Borrow the book"""
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"'{self.title}' has been borrowed!")
        else:
            print(f"'{self.title}' is already borrowed!")
    
    def return_book(self):
        """Return the book"""
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"'{self.title}' has been returned!")
        else:
            print(f"'{self.title}' is not borrowed!")
    
    def show_info(self):
        """Show book information"""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
        print(f"Status: {'Borrowed' if self.is_borrowed else 'Available'}")

# ========================================
# PART 2: POLYMORPHISM CHALLENGE
# ========================================

# Base class for animals
class Animal:
    
    def __init__(self, name):
        self.name = name
    
    def move(self):
        """How the animal moves - will be different for each animal"""
        pass
    
    def make_sound(self):
        """Sound the animal makes - will be different for each animal"""
        pass

# Dog class - inherits from Animal
class Dog(Animal):
    def move(self):
        """How dogs move"""
        print(f"{self.name} is running!")
    
    def make_sound(self):
        """Sound dogs make"""
        print(f"{self.name} says: Woof!")

# Cat class - inherits from Animal
class Cat(Animal):
    def move(self):
        """How cats move"""
        print(f"{self.name} is walking!")
    
    def make_sound(self):
        """Sound cats make"""
        print(f"{self.name} says: Meow!")

# Bird class - inherits from Animal
class Bird(Animal):
    def move(self):
        """How birds move"""
        print(f"{self.name} is flying!")
    
    def make_sound(self):
        """Sound birds make"""
        print(f"{self.name} says: Tweet!")

# ========================================
# TEST THE CLASSES
# ========================================

def test_book():
    print("=== BOOK CLASS TEST ===")
    
    # Create a book
    book1 = Book("Harry Potter", "J.K. Rowling", 300)
    
    # Test book methods
    book1.show_info()
    book1.borrow()
    book1.show_info()
    book1.return_book()
    book1.show_info()

def test_animals():
    """Test the Animal classes and polymorphism"""
    print("\n=== ANIMAL POLYMORPHISM TEST ===")
    
    # Create different animals
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    bird = Bird("Tweety")
    
    # Put all animals in a list
    animals = [dog, cat, bird]
    
    # Test each animal
    print("Animals moving and making sounds:")
    for animal in animals:
        animal.move()       
        animal.make_sound() 
        print()

def main():
    # Test the classes
    test_book()
    test_animals()


if __name__ == "__main__":
    main()
