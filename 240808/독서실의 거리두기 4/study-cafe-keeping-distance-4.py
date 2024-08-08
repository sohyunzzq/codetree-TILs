n = int(input())
seat = list(input())
for i in range(n):
    seat[i] = int(seat[i])

ans = 0
for i in range(n):
    for j in range(i+1, n):
        if seat[i] == 0 and seat[j] == 0:
            seat[i], seat[j] = 1, 1 #0인 자리 두 개 찾아서 1로 바꿔주기

            mini = n
            for k in range(n): 
                for m in range(k+1, n):
                    if seat[k] == 1 and seat[m] == 1: #자리 차 있는 곳 두 개 찾아서 거리 재기
                        mini = min(mini, m - k)
                        break

            seat[i], seat[j] = 0, 0
            ans = max(ans, mini)

print(ans)