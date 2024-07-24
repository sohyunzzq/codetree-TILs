dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

index = 3
x, y = 0, 0

cmd = input()

for i in range(len(cmd)):
    if cmd[i] == "L":
        index = (index - 1 + 4) % 4
    elif cmd[i] == "R":
        index = (index + 1) % 4
    else:
        x = x + dx[index]
        y = y + dy[index]

print(x, y)