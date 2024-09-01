## 50분, 

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False


def move(num, x, y):
    global grid

    ### 위부터 시계 방향
    dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

    maxi = -1
    maxx, maxy = -1, -1
    for dr in range(8):
        nx, ny = x + dx[dr], y + dy[dr]
        if not in_range(nx, ny):
            continue

        temp = grid[nx * n + ny]
        if temp == []:
            continue
        if max(temp) > maxi:
            maxi = max(temp)
            maxx, maxy = nx, ny
        
    
    ### 갈 곳이 있는지 확인
    if maxi != -1:

        ### 지금 내가 있는 리스트에서 제거
        index = 0
        while grid[x * n + y][0] != num:
            grid[maxx * n + maxy].insert(index, grid[x * n + y].pop(0))
            index += 1

        grid[x * n + y].remove(num)
        grid[maxx * n + maxy].insert(index, num)


n, m = map(int, input().split())
grid = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        grid.append([temp[j]])
nums = list(map(int, input().split()))


for num in nums:
    for i in range(n * n):
        if num in grid[i]:
            move(num, i // n, i % n)
            break


for i in range(n * n):
    if grid[i] == []:
        print("None", end = " ")
    else:
        for item in grid[i]:
            print(item, end = " ")

    print()