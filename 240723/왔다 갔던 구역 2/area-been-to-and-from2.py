n = int(input())

'''
총 n번
10번 왼쪽으로 간다면

- 10*n ~ 10*n 이 최대 구간임
: 0 ~ 20*n을 구간으로 잡고,
만약 n=1일 때는
-10 ~ 10인데
중간이 0
0 ~ 20, 중간이 10

10 L 이 들어오면
현재 위치부터 10칸 왼쪽까지 다 1을 더해줌
now부터 now-10까지
'''
area = [0] * (10*n*2+1)
now = 10*n

for i in range(n):
    num, p = input().split()
    if p == "L":
        for j in range(now, now-int(num), -1):
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