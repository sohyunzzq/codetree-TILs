n = int(input())
lst = list(map(int, input().split()))

lst.sort()

ans = 0
for k in range(lst[0] + 1, 101):
    cnt = 0
    for i in range(n): #ai
        for j in range(i+1, n): #aj
            if lst[j] - k == k - lst[i]:
                cnt += 1
    ans = max(ans, cnt)
print(ans)