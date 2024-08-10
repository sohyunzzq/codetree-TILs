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
#왼쪽은 가장 큰 거랑 얼마나 차이나는지
#오른쪽은 가장 작은 거랑 얼마나 차이나는지

#왼쪽은 최솟값, 오른쪽은 최댓값을 구하기
'''
22 27
10 100 :
25 26
'''