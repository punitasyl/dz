class Product:

    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category
    
    def apply_discount(self, discount: float):
        self.price -= self.price * discount

product1 = Product("Laptop", 1000.0, "Electronics")
print(f"Product: {product1.name}, Price: {product1.price}, Category: {product1.category}")
product1.apply_discount(0.1)
print(f"After discount, Price: {product1.price}")