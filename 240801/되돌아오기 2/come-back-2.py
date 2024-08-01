dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

cmd = input()

x, y = 0, 0
dir_num = 0
result = -1
time = 0

for i in range(len(cmd)):
    time += 1
    if cmd[i] == "F":
        x += dx[dir_num]
        y += dy[dir_num]

        if x == 0 and y == 0:
            result = time
            break

    elif cmd[i] == "L":
        dir_num = (dir_num - 1 + 4) % 4
    else:
        dir_num = (dir_num + 1) % 4
    
print(result)