def square(n):
    if n < 10:
        return n*n
    
    return square(n // 10) + square(n % 10)

n = int(input())
print(square(n))