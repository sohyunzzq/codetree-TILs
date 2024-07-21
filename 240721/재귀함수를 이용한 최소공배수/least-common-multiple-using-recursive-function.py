def lcd(n):
    if n == 0:
        return lst[0]

    for i in range(min(lst[n-1], lst[n]), lst[n-1] * lst[n] + 1, min(lst[n-1], lst[n])):
        if i % max(lst[n-1], lst[n]) == 0:
            lst[n-1] = i
            return lcd(n-1)

n = int(input())
lst = list(map(int, input().split()))
print(lcd(n-1))