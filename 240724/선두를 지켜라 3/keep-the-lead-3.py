n, m = map(int, input().split())

A = [0]
B = [0]
Anow = 0
Bnow = 0

for i in range(n):
    v, t = map(int, input().split())

    for i in range(t):
        A.append(Anow + v)
        Anow += v

for i in range(m):
    v, t = map(int, input().split())

    for i in range(t):
        B.append(Bnow + v)
        Bnow += v

#0 1 2 6 7 9 11 13 15 17 19 21 23 25 27
#0 2 4 6 7 8 11 14 17 20 23 26 29 32 35
#  1   2   3  4  5

cnt = 0
for i in range(1, len(A)):
    if ((A[i-1] == B[i-1] and (A[i] > B[i] or A[i] < B[i])) or (A[i-1] > B[i-1] and A[i] <= B[i]) or (A[i-1] < B[i-1] and A[i] >= B[i])):
        cnt += 1
print(cnt)