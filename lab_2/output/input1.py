@dataclass
class User:
    id: float
    name: str
    email: str
    age: float
    isActive: bool

@dataclass
class Product:
    id: float
    title: str
    price: float

def createUser1(id: float, name: str, email: str, age: float) -> User:
    return {
    id: id,
    name: name,
    email: email,
    age: age,
    isActive: True
    }

def calculateDiscount1(price: float, percent: float) -> float:
    return price - price * percent / 100

isAdult1 = lambda age: age >= 18  # type: (float) -> bool

increasePrice1 = lambda price: price + 10  # type: (float) -> float

def printUserName1(user: User) -> None:
    print(user.name)