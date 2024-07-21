def sum_rec(n):
    if n < 10:
        return n
    
    return sum_rec(n // 10) + sum_rec(n % 10)

a, b, c = map(int, input().split())
print(sum_rec(a*b*c))