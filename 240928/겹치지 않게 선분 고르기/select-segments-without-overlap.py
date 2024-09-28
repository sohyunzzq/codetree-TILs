n = int(input())
line = []
for i in range(n):
    line.append(list(map(int, input().split())))
line.sort(key = lambda x: (-x[1], -x[0]))

maxi = 0
for i in range(n):
    cnt = 1
    last = line[i]
    for j in range(i+1, n):
        if last[0] > line[j][1]:
            cnt += 1
            last = line[j]
    
    maxi = max(maxi, cnt)

print(maxi)