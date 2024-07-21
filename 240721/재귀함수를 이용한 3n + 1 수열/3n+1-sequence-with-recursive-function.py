def seq(n):
    if n == 1:
        return 0

    if n % 2 == 0:
        return 1 + seq(n // 2)
    else:
        return 1 + seq(3 * n + 1)

n = int(input())
print(seq(n))