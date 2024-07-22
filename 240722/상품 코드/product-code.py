class Product:
    def __init__(self, name = "codetree", code = "50"):
        self.name = name
        self.code = code

name, code = input().split()

p1 = Product()
p2 = Product(name, code)

print("product {} is {}".format(p1.code, p1.name))
print("product {} is {}".format(p2.code, p2.name))