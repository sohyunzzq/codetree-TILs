n = int(input())
lst = list(map(int, input().split()))

lst.sort()
maxi = 0
for i in range(n):
    tmp = lst[i] + lst[::-1][i]
    if tmp > maxi:
        maxi = tmp

print(maxi)