n = int(input())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))

ans = 0
for row in range(n-2):
    for col in range(n-2):
        #왼쪽 위가 갈 수 있는 범위
        cnt = 0
        for i in range(3):
            for j in range(3):
                if area[row + i][col + j]:
                    cnt += 1
        ans = max(ans, cnt)

print(ans)