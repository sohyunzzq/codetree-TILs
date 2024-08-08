import sys

n, k = map(int, input().split())
lst = list(map(int, input().split()))

#[i, i+k]
#i보다 작으면 i까지 올려주고
#i+k보다 크면 i+k까지 낮춰줌

ans = sys.maxsize
for i in range(10001):
    cost = 0
    for j in range(n):
        if lst[j] < i:
            cost += i - lst[j]
        elif lst[j] > i + k:
            cost += lst[j] - (i + k)
    
    ans = min(ans, cost)

print(ans)