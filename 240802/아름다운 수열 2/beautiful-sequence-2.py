n, m = map(int, input().split())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

cnt = 0

for i in range(n-m+1):
    if sorted(lst1[i:i+m]) == sorted(lst2):
        cnt += 1

print(cnt)