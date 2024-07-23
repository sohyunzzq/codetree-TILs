n, m = map(int, input().split())

A = []
B = []
Anow, Bnow = 0, 0

for i in range(n):
    pos, num = input().split()
    
    if pos == "L":
        for j in range(Anow - 1, Anow - int(num) - 1, -1):
            A.append(j)
        Anow -= int(num)
    else:
        for j in range(Anow + 1, Anow + int(num) + 1):
            A.append(j)
        Anow += int(num)

for i in range(m):
    pos, num = input().split()
    
    if pos == "L":
        for j in range(Bnow - 1, Bnow - int(num) - 1, -1):
            B.append(j)
        Bnow -= int(num)
    else:
        for j in range(Bnow + 1, Bnow + int(num) + 1):
            B.append(j)
        Bnow += int(num)

for i in range(1, min(len(A), len(B))):
    if A[i] == B[i]:
        print(i+1)
        break
if i == min(len(A), len(B)):
    print(-1)