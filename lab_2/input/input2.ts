interface User {
  id: number;
  name: string;
  email: string;
  age: number;
  isActive: boolean;
}

interface Product {
  id: number;
  title: string;
  price: number;
  inStock: boolean;
}

function createUser2(id: number, name: string, email: string, age: number): User {
  return {
    id: id,
    name: name,
    email: email,
    age: age,
    isActive: true
  };
}

function createProduct(id: number, title: string, price: number): Product {
  return {
    id: id,
    title: title,
    price: price,
    inStock: true
  };
}

function calculateDiscount2(price: number, percent: number): number {
  return price - price * percent / 100;
}

const isAdult2 = (age: number): boolean => age >= 18;
const increasePrice2 = (price: number): number => price + 10;

const printUserName2 = (user: User): void => {
  console.log(user.name);
};

const printProductTitle = (product: Product): void => {
  console.log(product.title);
};

function toggleActive(user: User): User {
  user.isActive = !user.isActive;
  return user;
}
