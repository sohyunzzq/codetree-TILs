def fibo(n):
    if n == 1 or n == 2:
        return 1
    
    return fibo(n-1) + 1

n = int(input())
print(fibo(n))