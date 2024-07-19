n = int(input())
for i in range(1, n+1):
    for j in range(1, n-i+2):
        print("{} * {} = {}".format(i, j, i*j), end = "")
        if i != n-j+1:
            print(" / ", end = "")
    print()