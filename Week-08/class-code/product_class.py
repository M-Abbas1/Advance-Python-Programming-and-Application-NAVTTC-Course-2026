class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_price(self, new_price):
        self.price = new_price
        print("price updated successfully!")

    def check_availability(self):
        return self.stock
            



products = []

for i in range(1, ):
    print(f"Creating Product {i}")
    n = input("Etner Product Name : ")
    p = float(input("Enter Product Price : "))
    s = int(input("Enter Product Stock : "))

    product = Product(n, p, s)

    print("Product Created Successfully!")

    products.append(product)

    print("Product appended into products list")

    print("*"*20)