n = int(input())
seat = list(input())
for i in range(n):
    seat[i] = int(seat[i])

maxi = 0
for i in range(n):
    for j in range(i+1, n):
        if seat[i] == 1 and seat[j] == 1:
            if j - i > maxi:
                maxi = max(maxi, j - i)
                s1 = i
                s2 = j
            break

seat[s1+(s2-s1)//2] = 1
   
mini = n
for i in range(n):
    for j in range(i+1, n):
        if seat[i] == 1 and seat[j] == 1:
            mini = min(mini, j-i)

#맨 마지막에 배치했을 때가 중간에 끼워넣은 것보다 멀다면?
#거리를 잰 후, 중간 끼웠을 때랑 비교해서 맨 마지막에 넣는 게 더 멀면 
         
if seat[n-1] == 0:
    for i in range(n-1, -1, -1):
        if seat[i] == 1:
            dis = n-1 - i
            break
    if dis > mini:
        seat[s1+(s2-s1)//2] = 0
        seat[n-1] = 1


mini = n
for i in range(n):
    for j in range(i+1, n):
        if seat[i] == 1 and seat[j] == 1:
            mini = min(mini, j-i)

print(mini)