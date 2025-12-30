interface Person {
  name: string;
  age: number;
  isStudent: boolean;
}

interface Book {
  title: string;
  pages: number;
}

function greet(name: string): void {
  console.log(`Hello, ${name}!`);
}

function add(x: number, y: number): number {
  const result = x + y;
  return result;
}

function createPerson(name: string, age: number, isStudent: boolean): Person {
  return {
      name: name,
      age: age,
      isStudent: isStudent
  };
}

function updateBook(book: Book, newTitle: string): Book {
  const updated = { title: newTitle, pages: book.pages };
  console.log(`Book updated to: ${newTitle}`);
  return updated;
}

const isAdult = (person: Person): boolean => {
  return person.age >= 18;
};

const numbers = [1, 2, 3, 4, 5];

const users = [
  { name: "Alice", age: 25, isStudent: false },
  { name: "Bob", age: 17, isStudent: true }
];

const double = (x: number): number => x * 2;

function createDefaultPerson(): Person {
  return {
      name: "Unknown",
      age: 0,
      isStudent: false
  };
}
