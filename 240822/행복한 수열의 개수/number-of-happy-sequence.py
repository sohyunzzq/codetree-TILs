def row(i, j):
    for k in range(m):
        if lst[i][j] != lst[i][j+k]:
            return False
    return True

def col(i, j):
    for k in range(m):
        if lst[j][i] != lst[j+k][i]:
            return False
    return True

n, m = map(int, input().split())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

ans = 0
for i in range(n):
    check = False
    for j in range(n-m+1):
        if not check:
            if row(i, j):
                check = True
                ans += 1

for i in range(n):
    check = False
    for j in range(n-m+1):
        if not check:
            if col(i, j):
                check = True
                ans += 1

print(ans)