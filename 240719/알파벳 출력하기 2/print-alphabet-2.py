str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(input())
index = 0

for i in range(n):
    for j in range(i):
        print("  ", end = "")
    for j in range(n-i):
        print(str1[index], end = " ")
        index += 1
        if index > 25:
            index = 0
    print()