def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

dict1 = {0: 1, 1: 0, 2: 3, 3: 2}
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

n = int(input())

area = []
for i in range(n):
    area.append(input())

k = int(input())
if 1 <= k <= 1 * n:
    dir_num = 2
    x = 0
    y = k - 1
elif 1 * n < k <= 2 * n:
    dir_num = 3
    x = k % n - 1
    y = n - 1
elif 2 * n < k <= 3 * n:
    dir_num = 0
    x = n - 1
    y = n - k % n
else:
    dir_num = 1
    x = n - k % n
    y = 0

cnt = 0
while True:
    if not in_range(x, y):
        print(cnt)
        break

    if area[x][y] == "/":
        dir_num = dict1[dir_num]
    else:
        dir_num = 3 - dir_num

    x += dx[dir_num]
    y += dy[dir_num]
    cnt += 1