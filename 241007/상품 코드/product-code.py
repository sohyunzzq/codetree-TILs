import sys

class product:
    def __init__(self, name = "codetree", code = 50):
        self.name = name
        self.code = code

tmp = sys.stdin.readline().rstrip().split()
products = [
    product(),
    product(tmp[0], tmp[1])
]

for p in products:
    print("product", p.code, "is", p.name)