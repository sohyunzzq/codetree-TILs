n = int(input())
lst = list(map(int, input().split()))

lst.sort(reverse = True)

min1 = lst[0]
for i in range(n-1):
    if lst[i] - lst[i+1] < min1:
        min1 = lst[i] - lst[i+1]

print(min1)