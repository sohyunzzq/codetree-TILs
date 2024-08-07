def jump(x):
    tmp = [0]
    for index, item in enumerate(lst):
        if index <= x:
            tmp.append(item)
    tmp.append(n-1)
    for i in range(len(tmp) - 1):
        if tmp[i+1] - tmp[i] > k:
            return False
    return True

n, k = map(int, input().split())
lst = list(map(int, input().split()))

#1번에서 시작해서 마지막에 도달해야 함
#최댓값이 최소가 되도록
#2 3 5 4 1

temp = set(sorted(lst, reverse = True))
ans = max(lst)
for i in temp:
    if jump(i):
        ans = min(ans, i)
print(ans)