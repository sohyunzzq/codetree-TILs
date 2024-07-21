def sum_rec(n):
    if n == 1:
        return 1
    
    return n + sum_rec(n-1)

total = 0
n = int(input())
total += sum_rec(n)
print(total)