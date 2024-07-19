def func(n, m):
    for i in range(max(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            return i

n, m = map(int, input().split())
print(func(n, m))