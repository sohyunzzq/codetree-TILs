def iseven(n):
    total = 0
    for i in range(len(str(n))):
        total += int(str(n)[i])
    if total % 2 == 0:
        return True
    return False

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

a, b = map(int, input().split())
cnt = 0

for i in range(a, b+1):
    if isprime(i) and iseven(i):
        cnt += 1

print(cnt)