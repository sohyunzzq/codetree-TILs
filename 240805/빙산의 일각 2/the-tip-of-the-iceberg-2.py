def up(iceberg, height):
    if iceberg > height:
        return 1
    return 0

n = int(input())

iceberg = []
for i in range(n):
    iceberg.append(int(input()))

# 010000100
# 1101011001 이런 식으로 있다고 쳤을 때
# 1 뭉텅이가 몇 개인지 세야 함

ans = 0
for i in range(max(iceberg)):
    check = [0] * n
    for j in range(n):
        if iceberg[j] > i:
            check[j] = 1

    cnt = 0
    p = 0
    for j in range(n):
        if check[j] == 1 and p == 0:
            cnt += 1
        p = check[j]
    ans = max(ans, cnt)

print(ans)