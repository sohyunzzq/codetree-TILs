n = int(input())
lst = list(map(int, input().split()))

lst.sort()

mini = max(lst)
for i in range(n):
    mini = min(mini, lst[i + n] - lst[i])

print(mini)