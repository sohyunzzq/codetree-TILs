import sys

cmd = sys.stdin.readline()

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
x, y = 0, 0
dr = 3

for letter in cmd:
    if letter == "L":
        dr = (dr - 1 + 4) % 4
    elif letter == "R":
        dr = (dr + 1) % 4
    else:
        x += dx[dr]
        y += dy[dr]

print(x, y)