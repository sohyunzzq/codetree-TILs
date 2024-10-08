n = int(input())

lst = []
for i in range(n):
    a, b = map(int, input().split())
    if a != b:
        lst.append([a, b])

#가능한 경우: 1 - 2 - 3 - 1 / 1 - 3 - 2 - 1

game = [
    {1: 2, 2: 3, 3: 1}, #키를 값이 이김 = 2가 1을 이김
    {1: 3, 3: 2, 2: 1},
]

ans = 0
for i in game:
    tmp = 0
    for j in lst:
        if i[j[0]] == j[1]:
            tmp += 1
    ans = max(ans, tmp)

print(ans)