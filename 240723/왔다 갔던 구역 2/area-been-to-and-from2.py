n = int(input())

area = [0] * (20*n+1)
now = 10*n

for i in range(n):
    num, p = input().split()
    if p == "L":
        for j in range(now-int(num), now):
            area[j] += 1
        now -= int(num)
    else:
        for j in range(now, now+int(num)):
            area[j] += 1
        now += int(num)

area.sort(reverse=True)

cnt = 0
for i in area:
    if i < 2:
        break
    cnt += 1

print(cnt)