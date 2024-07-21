def rem(n):
    if n == 1:
        return 2
    if n == 2:
        return 4
    
    return rem(n-1) * rem(n-2) % 100

n = int(input())
print(rem(n))