n = int(input())

lst = [0] * 201
for i in range(n):
    a, b = map(int, input().split())
    for j in range(a, b):
        lst[j+100] += 1

print(max(lst))