import sys

cmd = sys.stdin.readline().rstrip()

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


def comeback():
    dr = 3
    x, y = 0, 0
    t = 0

    for letter in cmd:
        t += 1

        if letter == "L":
            dr = (dr - 1 + 4) % 4
        elif letter == "R":
            dr = (dr + 1) % 4
        else:
            x += dx[dr]
            y += dy[dr]

            if x == 0 and y == 0:
                return t
    
    return -1

print(comeback())