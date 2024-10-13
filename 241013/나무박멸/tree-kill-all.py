def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def get_cnt():
    #모든 칸 순회해서 수 센 다음 리스트 반환
    cnt = []
    for i in range(n):
        cnt.append([0] * n)

    #오른쪽 위부터 시계 방향
    dx, dy = [-1, 1, 1, -1], [1, 1, -1, -1]
    for row in range(n):
        for col in range(n):
            #나무가 있는 곳에만 뿌릴 수 있음
            if area[row][col] > 0:
                #내 칸 먼저 죽여
                cnt[row][col] += area[row][col]

                #대각선으로 각각 k칸씩 뻗기
                x, y = row, col
                for dr in range(4):
                    for i in range(1, k + 1):
                        nx, ny = x + dx[dr] * i, y + dy[dr] * i

                        if not in_range(nx, ny) or area[nx][ny] == 0 or area[nx][ny] == -1:
                            break

                        if sprays[nx][ny] > 0:
                            continue

                        cnt[row][col] += area[nx][ny]
    return cnt

def findmax(lst):
    maxi = 0
    for row in lst:
        maxi = max(maxi, max(row))

    return maxi

def start(x, y):
    #[x, y]에 제초제 뿌려서 나무들 다 죽여
    #내 칸 먼저 죽이고 제초제 리스트에 추가하기
    area[x][y] = 0
    sprays[x][y] = c

    # 오른쪽 위부터 시계 방향
    dx, dy = [-1, 1, 1, -1], [1, 1, -1, -1]

    # 대각선으로 각각 k칸씩 뻗기
    for dr in range(4):
        for i in range(1, k + 1):
            nx, ny = x + dx[dr] * i, y + dy[dr] * i

            #벽이 있거나 격자 벗어나면 나가
            if not in_range(nx, ny) or area[nx][ny] == -1:
                break

            #텅 비었으면 여기까지 뿌리고 나가
            if area[nx][ny] == 0:
                sprays[nx][ny] = c
                break

            sprays[nx][ny] = c
            area[nx][ny] = 0

def GROW():
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    for row in range(n):
        for col in range(n):
            #벽이 아니고 제초제도 아니고 나무가 있는 곳만
            if area[row][col] > 0:
                x, y = row, col
                cnt = 0

                for dr in range(4):
                    nx, ny = x + dx[dr], y + dy[dr]

                    if in_range(nx, ny) and area[nx][ny] > 0:
                        cnt += 1

                area[row][col] += cnt

def SPREAD():
    #기존 나무 찾기 위해 새로운 리스트 만듦
    new_area = []
    for i in range(n):
        new_area.append([0] * n)

    for row in range(n):
        for col in range(n):
            new_area[row][col] = area[row][col]

    #기존 나무 인접 4칸 중 텅 빈 칸에 번식
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    for row in range(n):
        for col in range(n):
            #내 칸이 나무 있는 나무
            if area[row][col] > 0:
                cnt = 0
                x, y = row, col

                for dr in range(4):
                    nx, ny = x + dx[dr], y + dy[dr]

                    if in_range(nx, ny) and area[nx][ny] == 0 and sprays[nx][ny] == 0:
                        cnt += 1

                for dr in range(4):
                    nx, ny = x + dx[dr], y + dy[dr]

                    if in_range(nx, ny) and area[nx][ny] == 0 and sprays[nx][ny] == 0:
                        new_area[nx][ny] += area[row][col] // cnt

    #새로 만든 리스트 복제
    for row in range(n):
        for col in range(n):
            area[row][col] = new_area[row][col]

def WORK():
    global ans

    #모든 칸 돌면서 몇 칸 죽일 수 있는지 일일이 세보기
    cnt = get_cnt()

    #가장 많은 수 찾고, 그 값이랑 같은 애들 좌표 추가하기
    maxi = findmax(cnt)
    candi = []
    for row in range(n):
        for col in range(n):
            if cnt[row][col] == maxi:
                candi.append([row, col])

    #정렬한 후 그 좌표에 뿌리기
    candi.sort(key = lambda x: (x[0], x[1]))
    start(candi[0][0], candi[0][1])
    ans += maxi

def DEC():
    for row in range(n):
        for col in range(n):
            if sprays[row][col] > 0:
                sprays[row][col] -= 1

n, m, k, c = map(int, input().split())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))
sprays = []
for i in range(n):
    sprays.append([0] * n)

ans = 0
for year in range(1, m + 1):
    #전체 리스트 순회하며 나무 성장시키기
    GROW()

    #전체 리스트 순회하며 나무 번식시키기
    SPREAD()

    #제초제 수명 깎기
    DEC()

    #제초제 작업
    WORK()

print(ans)