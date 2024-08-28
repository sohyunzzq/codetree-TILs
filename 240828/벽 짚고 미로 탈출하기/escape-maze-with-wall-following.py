def is_wall(x, y):
    if grid[x][y] == "#":
        return True
    return False

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

n = int(input())
start_x, start_y = map(int, input().split())
grid = []
for i in range(n):
    grid.append([0] * n)

for i in range(n):
    tmp = input()
    for j in range(n):
        grid[i][j] = tmp[j]

start_x -= 1
start_y -= 1

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
dr = 1


t = 0

#바로 앞에 벽이 있으면 반시계 회전
#오른쪽을 보고 벽이 있으면 전진함
#오른쪽에 벽이 없으면 시계방향으로 회전
#처음 위치로 돌아오면 -1
#밖으로 나가면 break

x, y = start_x, start_y
while True:
    if in_range(x + dx[dr], y + dy[dr]) and is_wall(x + dx[dr], y + dy[dr]): #바로 앞에 벽
        dr = (dr - 1 + 4) % 4 #반시계 회전
    
    dr_right = (dr + 1) % 4
    if in_range(x + dx[dr_right], y + dy[dr_right]):
        if not is_wall(x + dx[dr_right], y + dy[dr_right]):
            dr = dr_right
        x += dx[dr]
        y += dy[dr]
        t += 1
    
    if x == start_x and y == start_y:
        t = -1
        break
    
    if not in_range(x, y):
        break
    
    
    
    
print(t)