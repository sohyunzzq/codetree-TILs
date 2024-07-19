def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def sum_n(a, b):
    total = 0
    for i in range(a, b+1):
        if prime(i):
            total += i
    return total

a, b = map(int, input().split())
print(sum_n(a, b))