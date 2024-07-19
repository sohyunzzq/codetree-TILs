lst = list(map(int, input().split()))

for i in range(10):
    if lst[i] % 3 == 0:
        print(lst[i-1])
        break