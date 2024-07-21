n = int(input())

lst = list(map(int, input().split()))
lst2 = []
for i in lst:
    lst2.append(i)
    if i % 2 == 1:
        lst3 = sorted(lst2)
        print(lst3[len(lst3)//2], end = " ")