import sys

n = int(input())

hill = []
for i in range(n):
    hill.append(int(input()))

#범위를 설정할 거임, [i, i+17] 이내에 들어오는지 순회하면서 찾아보기
#첫 i는 0부터 100-17
#i보다 낮은 건 i와, i+17보다 높은 건 i+17과의 차이를 구해서 제곱한 후 비용 구하기

ans = sys.maxsize

for i in range(100 - 17):
    cost = 0

    for j in range(n):
        if hill[j] < i:
            cost += (i-hill[j]) ** 2
        elif hill[j] > i + 17:
            cost += (hill[j] - (i + 17)) ** 2
    
    ans = min(ans, cost)

print(ans)