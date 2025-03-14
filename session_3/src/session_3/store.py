
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name} costs ${self.price:.2f}"

    def __repr__(self):
        return f"Product({self.name!r}, {self.price!r})"


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return f"User: {self.username}, Email: {self.email}"


class Store:
    def __init__(self):
        self.stock = {}

    def add_stock_product(self, product: Product, quantity: int):
        if product.name in self.stock:
            self.stock[product.name]["stock"] += quantity
            print(f"{self.stock}")
        else:
            print(f"the {product.name} does not exists in stock")


    def addProduct(self, product: Product, quantity: int):
        if product.name in self.stock:
            self.stock[product.name]["stock"] += quantity
            print(f"{self.stock}")

        else:
            self.stock[product.name] = {"price:": product.price, "stock": quantity}
            print(f"{self.stock}")


class Admin:
    def __init__(self):
        self.users = {}

    def newUser(self,user:User):
        if user in self.users:
            print("the user already exist")
        else:
            self.users = user
            print(f"New user added {user}")



cereais = Product("Cereais", 3.50)
user = User("Nelson","nelson@gmail.com")

if __name__ == __name__:
    Store().addProduct(cereais, 1)
    Admin().newUser(user)
    Store().add_stock_product(cereais,5)
