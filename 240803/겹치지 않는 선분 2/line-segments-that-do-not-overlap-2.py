n = int(input())

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))
lst.sort(key = lambda x: min(x[0], x[1]))

#언제 겹치는가?
#다른 선분의 두 좌표가 모두 다른 선분의 두 좌표 사이에 있을 때

check = [1] * n
for i in range(n):
    x1, x2 = lst[i][0], lst[i][1]
    for j in range(i+1, n):
        x3, x4 = lst[j][0], lst[j][1]
        if x1 <= x2 and x3 <= x4: #// 방향
            if x1 <= x3 <= x2 and x1 <= x4 <= x2:
                check[i] = 0
                check[j] = 0
        elif x1 >= x2 and x3 >= x4: #\\ 방향
            if x2 <= x3 <= x1 and x2 <= x4 <= x1:
                check[i] = 0
                check[j] = 0
        elif x1 <= x2 and x3 >= x4: #/\
            if x1 <= x4 <= x2 or x1 <= x3 <= x2:
                check[i] = 0
                check[j] = 0
        elif x1 >= x2 and x3 <= x4:
            if x2 <= x3 <= x1 or x2 <= x4 <= x1:
                check[i] = 0
                check[j] = 0

print(sum(check))