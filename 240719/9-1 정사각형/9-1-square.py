n = int(input())
index = 9
for i in range(n):
    for j in range(n):
        print(index, end="")
        index -= 1
        if index < 1:
            index += 9
    print()