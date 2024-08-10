n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

goal = sum(lst) // n
ans = 0

for i in lst:
    if i < goal:
        ans += goal - i

print(ans)