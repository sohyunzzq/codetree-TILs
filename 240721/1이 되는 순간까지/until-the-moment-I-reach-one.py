def recursive(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + recursive(n // 2)
    else:
        return 1 + recursive(n // 3)

n = int(input())
print(recursive(n))