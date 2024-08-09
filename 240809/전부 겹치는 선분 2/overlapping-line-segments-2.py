n = int(input())

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

check = False
for i in range(n):
    maxi = 0 #x1의 최댓값
    mini = 101 #x2의 최솟값

    for j in range(n):
        if i == j: #뺀 선분
            continue
        
        maxi = max(maxi, lst[j][0])
        mini = min(mini, lst[j][1])
    
    if maxi <= mini:
        check = True
        break

if check:
    print("Yes")
else:
    print("No")