n = int(input())
seat = list(input())
for i in range(n):
    seat[i] = int(seat[i])

#가장 먼 곳의 거리 구하기
maxi = 0
s1, s2 = 0, 0
for i in range(n):
    for j in range(i+1, n):
        if seat[i] == 1 and seat[j] == 1:
            if j - i > maxi:
                maxi = j - i
                s1, s2 = i, j
                break

mini1, mini2, mini3 = 0, 0, 0

#맨 앞자리가 비었고, 거기 들어간다면 최소 거리는?
if seat[0] == 0:
    mini1 = n
    seat[0] = 1
    for i in range(n):
        for j in range(i+1, n):
            if seat[i] == 1 and seat[j] == 1:
                mini1 = min(mini1, j - i)
    seat[0] = 0

#맨 뒷자리가 비었고, 거기 들어간다면 최소 거리는?
if seat[n-1] == 0:
    mini2 = n
    seat[n-1] = 1
    for i in range(n):
        for j in range(i+1, n):
            if seat[i] == 1 and seat[j] == 1:
                mini2 = min(mini2, j - i)
    seat[n-1] = 0

if s1 and s2:
    seat[s1 + (s2-s1) // 2] = 1

    mini3 = n
    for i in range(n):
        for j in range(i+1, n):
            if seat[i] == 1 and seat[j] == 1:
                mini3 = min(mini3, j - i)

print(max(mini1, mini2, mini3))