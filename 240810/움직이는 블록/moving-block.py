n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

goal = sum(lst) / n
ans = 0

for i in lst:
    if i < goal:
        ans += goal - i
    elif i > goal:
        ans += i - goal

print(int(ans // 2))