def up(iceberg, height):
    if iceberg > height:
        return 1
    return 0

n = int(input())

iceberg = []
for i in range(n):
    iceberg.append(int(input()))

# 1101011001 이런 식으로 있다고 쳤을 때
# 1 뭉텅이가 몇 개인지 세야 하는데
# 1번 인덱스부터 시작해서
# 0에서 1이 되면 cnt+1
# 0, 1번 중 하나라도 1이면 +1

ans = 0
for i in range(max(iceberg)):
    if n == 1:
        ans = 1
        break
    cnt = 0
    past = up(iceberg[0], i)
    if past + up(iceberg[1], i) != 0:
        cnt += 1
    for j in range(1, n):
        now = up(iceberg[j], i)
        if past == 0 and now == 1:
            cnt += 1
        past = now
    
    ans = max(ans, cnt)

print(ans)