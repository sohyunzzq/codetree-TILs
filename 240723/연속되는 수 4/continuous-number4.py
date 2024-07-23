n = int(input())

lst = []
for i in range(n):
    lst.append(int(input()))

ans = 0
cnt = 1
for i in range(n):
    if i >= 1 and lst[i] > lst[i-1]:
        cnt += 1
    else:
        cnt = 1
    ans = max(ans, cnt)
print(ans)