## 55분, 시간 초과 진짜 개억까네 ㅁㅊ

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False


def remove_bead():
    length = len(beads)
    new_beads = []
    grid = []
    for i in range(n):
        grid.append([0] * n)

    for bead in beads:
        grid[bead[0]][bead[1]] += 1
    
    for bead in beads:
        if grid[bead[0]][bead[1]] >= 2:
            continue
        
        new_beads.append(bead)
      
    return new_beads

'''
시간 초과

    for i in range(length):
        for j in range(i+1, length):
            if beads[i][0] == beads[j][0] and beads[i][1] == beads[j][1]:
                remove_lst.append(i)
                remove_lst.append(j)
    
    for i in range(length):
        if i not in remove_lst:
            new_beads.append(beads[i])
'''          


def one_second():
    length = len(beads)
    for i in range(length):
        x, y = beads[i][0], beads[i][1]
        dr = beads[i][2]
        nx, ny = x + dx[dr], y + dy[dr]

        ### 부딪히면 방향 바꾸기
        if not in_range(nx, ny):
            beads[i][2] = (dr + 2) % 4
        else:
            beads[i][0] = nx
            beads[i][1] = ny


def simul():
    global beads

    ### 2n번 이동을 해도 아무것도 안 부딪히면 리턴
    for i in range(2 * n):
        one_second()
        beads = remove_bead()
    
    return len(beads)


mapper = {"U": 0, "R": 1, "D": 2, "L": 3}
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

t = int(input())
for i in range(t):
    n, m = map(int, input().split())


    beads = []
    for j in range(m):
        x, y, dr = input().split()
        beads.append([int(x)-1, int(y)-1, mapper[dr]])
    
    ans = simul()
    print(ans)