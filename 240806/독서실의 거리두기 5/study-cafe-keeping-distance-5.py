n = int(input())
seat = list(input())

ans = 0
for i in range(n):
    if seat[i] == "0":
        seat[i] = "1"
    else:
        continue
    print(seat)
    tmp = n
    for j in range(n): #거리 세기
        if seat[j] == "1":
            dis = 1
            for k in range(j+1, n):
                if seat[k] == "1" or k == n-1:
                    break
                dis += 1
            if seat[n-1] == "0" and k != n-1:
                tmp = min(tmp, dis)
    print(tmp)
    ans = max(ans, tmp)
    seat[i] = "0"
print(ans)