n = int(input())
seat = list(input())
for i in range(n):
    seat[i] = int(seat[i])

ans = 0
for i in range(n):
    if seat[i] == 0:
        seat[i] = 1
    else:
        continue

    number = sum(seat)
    #자리를 배치했고, 이 배치에서 최소거리를 구함

    min_dis = n

    for j in range(n):
        for k in range(j+1, n):
            if seat[j] == 1 and seat[k] == 1: #여기서부터 다음 1까지의 거리를 구함
                min_dis = min(min_dis, abs(k-j))

    ans = max(ans, min_dis)
    seat[i] = 0
    
print(ans)