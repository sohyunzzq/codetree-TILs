def recursive(n):
    if n <= 2:
        return n
    
    return recursive(n-2) + n

n = int(input())
print(recursive(n))