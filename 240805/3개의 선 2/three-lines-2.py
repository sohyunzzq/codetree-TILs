n = int(input())

coor = []
for i in range(n):
    coor.append(list(map(int, input().split())))

#가능한 경우 (x/y에 평행한 선분 개수)
#x3 y0 
#x2 y1
#x1 y2
#x0 y3

#000, 001, ..., 101010 순회를 돌 거임
#x=0, x=0, x=0 이 경우 상관없음. 중복 안 된다는 말 없음
#000을 가지고 xxx, xxy, xyy, yyy 전부 다 검사를 할 거임
#000 - xxx - 좌표 이렇게 들어가서, 모든 좌표가 통과되면 result는 1

ans = 0

for i in range(11):
    for j in range(11):
        for k in range(11):
            check = True
            for x, y in coor:
                if x == i or x == j or x == k: #모두 x에 걸리냐
                    continue
                check = False
            
            if check:
                ans = 1

            check = True
            for x, y in coor:
                if x == i or x == j or y == k:
                    continue
                check = False
            
            if check:
                ans = 1

            for x, y in coor:
                if x == i or y == j or y == k:
                    continue
                check = False

            if check:
                ans = 1
            
            for x, y in coor:
                if y == i or y == j or y == k:
                    continue
                check = False
            
            if check:
                ans = 1

print(ans)