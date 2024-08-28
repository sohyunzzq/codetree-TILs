def max_row():
    for row in range(n):
        for col in range(k, k+m):
            if grid[row][col] == 1:
                return row - 1
    return n - 1

n, m, k = map(int, input().split())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))

#m이 크기, k가 블럭의 첫 번째 칸 위치

k -= 1
row = max_row()

for col in range(k, k+m):
    grid[row][col] = 1

for row in grid:
    for col in row:
        print(col, end = " ")
    print()