def add(a1, a2):
    total = 0
    for i in range(a1, a2+1):
        total += A[i-1]
    return total

n, m = map(int, input().split())
A = list(map(int, input().split()))
for i in range(m):
    a1, a2 = map(int, input().split())
    print(add(a1, a2))