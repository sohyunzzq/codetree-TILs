n, m = map(int, input().split())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

shapes = [[[0, 1, 1], [0, 0, 1]], [[0, 0, 1], [0, 1, 0]], [[0, 0, 1], [0, 1, 1]], [[0, 1, 1], [1, 0, 1]], [[0, 0, 0], [0, 1, 2]], [[0, 1, 2], [0, 0, 0]]]

def in_range(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

maxi = 0
for row in range(n):
    for col in range(m):
        x, y = row, col
        for shape in shapes:
            dx, dy = shape[0], shape[1]

            sum1 = 0
            for dr in range(3):
                nx, ny = x + dx[dr], y + dy[dr]

                if in_range(nx, ny):
                    sum1 += lst[nx][ny]

                maxi = max(maxi, sum1)

print(maxi)