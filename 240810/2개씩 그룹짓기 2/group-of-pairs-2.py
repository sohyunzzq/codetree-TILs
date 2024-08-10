n = int(input())
lst = list(map(int, input().split()))

#두 수의 차이의 최솟값이 최대가 되도록

lst.sort()

mini = max(lst)
for i in range(n):
    mini = min(mini, lst[i + n] - lst[i])

print(mini)


#2 5 7 9 10 15
#55 60 61 62 63 64 76 77