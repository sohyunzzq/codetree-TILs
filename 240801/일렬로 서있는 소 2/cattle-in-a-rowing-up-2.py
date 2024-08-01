n = int(input())
lst = list(map(int, input().split()))

cnt = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if lst[i] <= lst[j] <= lst[k]:
                cnt += 1

print(cnt)