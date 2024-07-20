def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return int(a // b)

a, o, c = input().split()
a = int(a)
c = int(c)

print("{} {} {} = ".format(a, o, c), end = "")
if o == "+":
    print(plus(a, c))
elif o == "-":
    print(minus(a, c))
elif o == "*":
    print(mul(a, c))
elif o == "/":
    print(div(a, c))
else:
    print("False")