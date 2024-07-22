n = int(input())

lst = [0] * 101
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, b+1):
        lst[i] += 1

print(max(lst))