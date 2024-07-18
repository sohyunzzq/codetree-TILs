n = int(input())

for i in range(n):
    print(" "*(n-i-1), end = "*")
    for j in range(i):
        print(" *", end = "")
    print()

for i in range(n-1):
    print(" "*i, end = "")
    print(" *"*(n-i-1), end = "")
    print()