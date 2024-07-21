n = int(input())
lst = list(map(int, input().split()))

lst.sort()

max = lst[0]
for i in range(n):
    if max < lst[i] + lst[::-1][i]:
        max = lst[i] + lst[::-1][i]

print(max)