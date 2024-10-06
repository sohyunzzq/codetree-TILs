import sys

n = int(sys.stdin.readline().rstrip())

dict1 = {"E": 0, "S": 1, "W": 2, "N": 3}
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def comeback():
    x, y = 0, 0
    t = 0
    
    for i in range(n):
        dr, num = sys.stdin.readline().rstrip().split()
        dr = dict1[dr]

        for j in range(int(num)):
            nx, ny = x + dx[dr], y + dy[dr]
            t += 1

            if nx == 0 and ny == 0:
                return t
            
            x, y = nx, ny
    
    return -1

print(comeback())