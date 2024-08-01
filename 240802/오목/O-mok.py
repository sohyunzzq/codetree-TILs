area = []
for i in range(19):
    area.append(list(map(int, input().split())))

ans = -1
for i in range(19):
    if ans != -1:
        break
    for j in range(19):
        if j < 19 - 4 and area[i][j] != 0 and area[i][j] == area[i][j+1] == area[i][j+2] == area[i][j+3] == area[i][j+4]:
            ans = area[i][j]
            x, y = i, j+2
            break
        if i < 19 - 4 and area[i][j] != 0 and area[i][j] == area[i+1][j] == area[i+2][j] == area[i+3][j] == area[i+4][j]:
            ans = area[i][j]
            x, y = i+2, j
            break
        if i < 19 - 4 and j < 19 - 4 and area[i][j] != 0 and area[i][j] == area[i+1][j+1] == area[i+2][j+2] == area[i+3][j+3] == area[i+4][j+4]:
            ans = area[i][j]
            x, y = i+2, j+2
            break
        if j >= 4 and i < 19 - 4 and area[i][j] != 0 and area[i][j] == area[i+1][j-1] == area[i+2][j-2] == area[i+3][j-3] == area[i+4][j-4]:
            ans = area[i][j]
            x, y = i+2, j-2
            break

if ans == -1:
    print(0)
else:
    print(ans)
    print(x+1, y+1)