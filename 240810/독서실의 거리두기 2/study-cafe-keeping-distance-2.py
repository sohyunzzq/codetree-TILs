n = int(input())
seat = list(input())
for i in range(n):
    seat[i] = int(seat[i])

ans = 0
for i in range(n):
    if seat[i] == 0:
        dis = n
        seat[i] = 1
        for j in range(n):
            for k in range(j+1, n):
                if seat[j] == 1 and seat[k] == 1:
                    dis = min(dis, k - j)
                    break
        ans = max(ans, dis)
        seat[i] = 0
print(ans)