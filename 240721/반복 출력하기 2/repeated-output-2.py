def printhello(n):
    if n < 1:
        return
    
    printhello(n-1)
    print("HelloWorld")

n = int(input())
printhello(n)