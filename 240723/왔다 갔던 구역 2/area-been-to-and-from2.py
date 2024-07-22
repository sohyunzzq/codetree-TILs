n = int(input())

'''
총 n번
10번 왼쪽으로 간다면

- 10*n ~ 10*n 이 최대 구간임
: 0 ~ 20*n

수직선, 겹치는 구간 → 끝나는 구간 안 더해줌
10 L 이 들어오면
0, 10 이므로 0 ~ 9까지 1 더해줌
그 다음 now는 0이 됨
'''
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