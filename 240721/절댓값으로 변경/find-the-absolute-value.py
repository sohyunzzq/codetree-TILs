def cal_abs(lst):
    for i in range(len(lst)):
        if lst[i] < 0:
            lst[i] = -lst[i]

n = int(input())
lst = list(map(int, input().split()))
cal_abs(lst)

for i in lst:
    print(i, end = " ")