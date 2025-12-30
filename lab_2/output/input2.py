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
    inStock: bool

def createUser2(id: float, name: str, email: str, age: float) -> User:
    return {
    id: id,
    name: name,
    email: email,
    age: age,
    isActive: True
    }

def createProduct(id: float, title: str, price: float) -> Product:
    return {
    id: id,
    title: title,
    price: price,
    inStock: True
    }

def calculateDiscount2(price: float, percent: float) -> float:
    return price - price * percent / 100

isAdult2 = lambda age: age >= 18  # type: (float) -> bool

def printUserName2(user: User) -> None:
    print(user.name)

def printProductTitle(product: Product) -> None:
    print(product.title)

def toggleActive(user: User) -> User:
    user.isActive = not user.isActive
    return user