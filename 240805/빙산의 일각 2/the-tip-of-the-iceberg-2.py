n = int(input())

height = []
for i in range(n):
    height.append(int(input()))

ans = 0
for i in range(max(height)):
    cnt = 0
    for j in range(n-1):
        if height[j] > i and height[j+1] <= i:
            cnt += 1
    if height[n-2] <= i and height[n-1] > i:
        cnt += 1
    ans = max(ans, cnt)

print(ans)