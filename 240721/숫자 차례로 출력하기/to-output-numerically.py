n = int(input())

def print_f(n):
    if n == 0:
        return
    
    print_f(n-1)
    print(n, end = " ")

def print_b(n):
    if n == 0:
        return
        
    print(n, end = " ")
    print_b(n-1)

print_f(n)
print()
print_b(n)