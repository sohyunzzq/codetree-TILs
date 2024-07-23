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

p = 0
cnt = 0

if max(len(A), len(B)) == len(A):
    maxlen = len(A)
    minlen = len(B)
    maxrobot = A
    minrobot = B
else:
    maxlen = len(B)
    minlen = len(A)
    maxrobot = B
    minrobot = A

for i in range(minlen):
    if i >= 1 and A[i] == B[i] and B[i-1] != A[i-1]:
        cnt += 1

for i in range(minlen, maxlen):
    if maxrobot[i] == minrobot[minlen - 1]:
        cnt += 1
print(cnt)