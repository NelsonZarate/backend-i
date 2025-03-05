store = {}


class Product():
    def __init__(self, name, price, stock: 0):
        self.name = name
        self.price = price
        self.stock = stock

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
    

def addProduct(name,price,stock):
    store[name] = {"price:":price,"stock:":stock}

def newUser():
    pass