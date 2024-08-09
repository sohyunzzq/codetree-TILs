n = int(input())
lst = list(map(int, input().split()))

lst2 = sorted(lst)
val = -1
for i in range(1, n):
    if lst2[i] == lst2[i-1]:
        continue
    val = lst2[i]
    break

cnt = 0
if val >= 1:
    for i in range(n):
        if lst[i] == val:
            answer = i
            cnt += 1

if val == -1 or cnt >= 2:
    print(-1)
else:
    print(answer)