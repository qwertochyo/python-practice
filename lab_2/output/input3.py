@dataclass
class Person:
    name: str
    age: float
    isStudent: bool

@dataclass
class Book:
    title: str
    pages: float

def greet(name: str) -> None:
    print(f"Hello, {name}not ")

def add(x: float, y: float) -> float:
    result = x + y
    return result

def createPerson(name: str, age: float, isStudent: bool) -> Person:
    return {
    name: name,
    age: age,
    isStudent: isStudent
    }

def updateBook(book: Book, newTitle: str) -> Book:
    updated = { title: newTitle, pages: book.pages }
    print(f"Book updated to: {newTitle}")
    return updated

def isAdult(person: Person) -> bool:
    return person.age >= 18

numbers = [1, 2, 3, 4, 5]

users = [
  { name: "Alice", age: 25, isStudent: False },
  { name: "Bob", age: 17, isStudent: True }
]

double = lambda x: x * 2  # type: (float) -> float

def createDefaultPerson() -> Person:
    return {
    name: "Unknown",
    age: 0,
    isStudent: False
    }