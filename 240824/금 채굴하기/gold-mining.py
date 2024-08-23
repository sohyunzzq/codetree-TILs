def exceed(k, cnt):
    if k*k + (k+1)*(k+1) > cnt * m: #손해
        return False
    return True

n, m = map(int, input().split())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))

maxi = 0
for i in range(n):
    for j in range(n): #중심의 좌표가 (i, j)
        for k in range(2 * (n-1) + 1):
            cnt = 0
            for x in range(n):
                for y in range(n):
                    if abs(i-x) + abs(j-y) <= k:
                        if area[x][y] == 1:
                            cnt += 1
            if exceed(k, cnt):
                maxi = max(maxi, cnt)

print(maxi)

#모든 격자를 커버하는 K를 따져보자
#격자가 2*2일 때 K는 2
#격자가 3*3일 때 K는 4
#격자가 4*4일 때 K는 6
#즉, 2*(n-1)가 K의 최댓값

#마름모는, 중앙을 기준으로
#x좌표차 + y좌표차 <= k (각각으로 하면 직사각형 될 듯)