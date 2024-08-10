n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

ans = 200
for i in range(n):
    mini = 100
    maxi = 0
    for j in range(n):
        if i == j:
            continue
        mini = min(mini, lst[j][0])
        maxi = max(maxi, lst[j][1])
    
    ans = min(ans, maxi - mini)

print(ans)

#아몰라몰라완전탐색으로풀거임