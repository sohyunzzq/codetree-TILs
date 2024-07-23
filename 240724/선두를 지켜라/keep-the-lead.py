n, m = map(int, input().split())

A = []
B = []
Adis = 0
Bdis = 0

for i in range(n):
    v, t = map(int, input().split())
    
    for j in range(1, t+1):
        A.append(Adis + v*j)
    Adis += v*j

for i in range(m):
    v, t = map(int, input().split())

    for j in range(1, t+1):
        B.append(Bdis + v*j)
    Bdis += v*j

cnt = 0
for i in range(1, len(A)):
    if (A[i-1] >= B[i-1] and A[i] < B[i]) or (A[i-1] <= B[i-1] and A[i] > B[i]):
        cnt += 1
print(cnt)