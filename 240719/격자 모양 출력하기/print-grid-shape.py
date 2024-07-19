n, m = map(int, input().split())

pan = []
for i in range(n):
    pan.append([0]*n)

for i in range(m):
    x, y = map(int, input().split())
    pan[x-1][y-1] = x*y

for i in pan:
    for j in i:
        print(j, end = " ")
    print()