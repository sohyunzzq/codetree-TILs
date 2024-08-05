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

    index = 0
    min_dis = n

    for j in range(n):
        if seat[j] == 1 and index < number - 1: #여기서부터 다음 1까지의 거리를 구함
            dis = 0
            index += 1
            
            for k in range(j + 1, n):
                if seat[k] == 1:
                    dis += 1
                    break
                dis += 1
            
        min_dis = min(min_dis, dis)
    
    ans = max(ans, min_dis)

    seat[i] = 0
print(ans)