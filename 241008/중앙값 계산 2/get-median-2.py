n = int(input())
lst = list(map(int, input().split()))

for i in range(1, n + 1):
    if i % 2 == 1:
        print(sorted(lst)[i // 2], end = " ")