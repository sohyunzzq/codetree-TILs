n = int(input())
line = []
for i in range(n):
    line.append(list(map(int, input().split())))
line.sort(key = lambda x: (-x[1], -x[0]))

cnt = 1

last = line[0]
for i in range(n-1):
    if last[0] > line[i+1][1]:
        cnt += 1
        last = line[i+1]

print(cnt)