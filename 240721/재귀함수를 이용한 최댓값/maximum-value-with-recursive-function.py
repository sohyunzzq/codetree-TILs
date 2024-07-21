def max_rec(n):
    if n == 0:
        return lst[0]
    
    return max(max_rec(n-1), lst[n])

n = int(input())
lst = list(map(int, input().split()))

print(max_rec(n-1))