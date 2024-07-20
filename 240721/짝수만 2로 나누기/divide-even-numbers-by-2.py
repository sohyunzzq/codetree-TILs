def change(lst):
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst[i] = int(lst[i] // 2)

n = int(input())
lst = list(map(int, input().split()))
change(lst)

for i in lst:
    print(i, end = " ")