dict1 = {"E": 0, "S": 1, "W": 2, "N": 3}
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

n = int(input())

x, y = 0, 0
result = -1
time = 0

for i in range(n):
    if result != -1:
        break

    direction, distance = input().split()
    dir_num = dict1[direction]

    for j in range(int(distance)):
        time += 1
        x += dx[dir_num]
        y += dy[dir_num]

        if x == 0 and y == 0:
            result = time
            break

print(result)