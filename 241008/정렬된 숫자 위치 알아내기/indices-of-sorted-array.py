class num:
    def __init__(self, value, origin, change = 0):
        self.value = value
        self.origin = origin
        self.change = change

n = int(input())
lst = list(map(int, input().split()))

ans = []

for i in range(n):
    tmp = num(lst[i], i + 1)
    ans.append(tmp)

ans.sort(key = lambda x: x.value)

for i in range(n):
    ans[i].change = i + 1

ans.sort(key = lambda x: x.origin)

for item in ans:
    print(item.change, end = " ")