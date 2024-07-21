def sum_rec(n):
    if n == 0:
        return 0
    
    return n + sum_rec(n-1)

n = int(input())
print(sum_rec(n))