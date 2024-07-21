n = int(input())

lst = list(map(int, input().split()))
lst2 = []
for i in range(1, n+1):
    lst2.append(lst[i-1])
    if i % 2 == 1:
        lst3 = sorted(lst2)
        print(lst3[len(lst3)//2], end = " ")