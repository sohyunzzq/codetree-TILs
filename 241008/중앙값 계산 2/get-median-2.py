n = int(input())
lst = list(map(int, input().split()))
lst2 = []

for i in range(n):
    lst2.append(lst[i])

    if i % 2 == 0:
        print(sorted(lst2)[i // 2], end = " ")