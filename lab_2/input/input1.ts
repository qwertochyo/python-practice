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
}

function createUser1(
  id: number,
  name: string,
  email: string,
  age: number
): User {
  return {
      id: id,
      name: name,
      email: email,
      age: age,
      isActive: true
  };
}

function calculateDiscount1(
  price: number,
  percent: number
): number {
  return price - price * percent / 100;
}

const isAdult1 = (age: number): boolean => age >= 18;

const increasePrice1 = (price: number): number => price + 10;

const printUserName1 = (user: User): void => {
  console.log(user.name);
};
