n = int(input())

coor = []
for i in range(n):
    coor.append(list(map(int, input().split())))

ans = 100

for i in range(0, 101, 2): # x = i 직선 (세로선)
    for j in range(0, 101, 2): # y = j 직선 (가로선)
        a1, a2, a3, a4 = 0, 0, 0, 0 #제1사분면 ~ 제4사분면
        for x, y in coor:
            if x > i:
                if y > j:
                    a1 += 1
                else:
                    a4 += 1
            else:
                if y > j:
                    a2 += 1
                else:
                    a3 += 1
        ans = min(ans, max(a1, a2, a3, a4))

print(ans)