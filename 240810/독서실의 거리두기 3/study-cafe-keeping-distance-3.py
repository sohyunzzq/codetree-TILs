n = int(input())
seat = list(input())
for i in range(n):
    seat[i] = int(seat[i])

#가장 가까운 두 사람 거리 최댓값
#가장 먼 두 곳 찾아서 사이에 껴주기

maxdis = 0
for i in range(n):
    for j in range(i+1, n):
        if seat[i] == 1 and seat[j] == 1:
            if maxdis < j-i:
                maxdis = j-i
                s1 = i
                s2 = j
            break
seat[s1+(s2-s1)//2] = 1

ans = n
for i in range(n):
    for j in range(i+1, n):
        if seat[i] == 1 and seat[j] == 1:
            ans = min(ans, j-i)
            break
print(ans)