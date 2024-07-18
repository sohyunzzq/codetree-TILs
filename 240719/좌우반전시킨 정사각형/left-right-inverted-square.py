n = int(input())

for i in range(1, n+1):
    j = n * i
    while j >= i:
        print(j, end = " ")
        j -= i
    print()