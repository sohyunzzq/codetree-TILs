n, m = map(int, input().split())

A = []
B = []
Anow = 0
Bnow = 0

for i in range(n):
    t, d = input().split()

    if d == "L":
        for j in range(Anow - 1, Anow - int(t) - 1, -1): #7에서 4 L이면 6 5 4 3
            A.append(j)
        Anow -= int(t)
    else:
        for j in range(Anow + 1, Anow + int(t) + 1): #7에서 2 R이면 8 9
            A.append(j)
        Anow += int(t)

for i in range(m):
    t, d = input().split()

    if d == "L":
        for j in range(Bnow - 1, Bnow - int(t) - 1, -1): #7에서 4 L이면 6 5 4 3
            B.append(j)
        Bnow -= int(t)
    else:
        for j in range(Bnow + 1, Bnow + int(t) + 1): #7에서 2 R이면 8 9
            B.append(j)
        Bnow += int(t)

if len(A) > len(B):
    for i in range(len(B), len(A)):
        B.append(B[len(B)-1])
else:
    for i in range(len(A), len(B)):
        A.append(A[len(A)-1])

cnt = 0

for i in range(1, len(A)):
    if A[i] == B[i] and B[i-1] != A[i-1]:
        cnt += 1
print(cnt)