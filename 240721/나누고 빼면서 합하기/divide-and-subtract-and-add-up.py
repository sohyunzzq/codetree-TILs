def cal(m, lst):
    total = lst[m-1]
    while m > 1:
        if m % 2 == 1:
            m -= 1
        else:
            m = int(m/2)
        total += lst[m-1]
    return total

n, m = map(int, input().split())
lst = list(map(int, input().split()))

print(cal(m, lst))