n = int(input())

iceberg = []
for i in range(n):
    iceberg.append(int(input()))

# 010000100
# 1101011001 이런 식으로 있다고 쳤을 때
# 1 뭉텅이가 몇 개인지 세야 함

ans = 0
for i in range(max(iceberg)):
    cnt = 0
    if iceberg[0] > i:
        cnt += 1

    for j in range(1, n):
        if iceberg[j] > i and iceberg[j-1] <= i:
            cnt += 1
    ans = max(ans, cnt)

print(ans)