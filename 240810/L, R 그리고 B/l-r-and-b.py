lst = []
for i in range(10):
    lst.append(list(input()))

for i in range(10):
    for j in range(10):
        if lst[i][j] == "L":
            lx, ly = i, j
        elif lst[i][j] == "B":
            bx, by = i, j
        elif lst[i][j] == "R":
            rx, ry = i, j

#L에서 R을 피해 B로
#ㄴ 혹은 ㄱ 모양으로 가기
print(abs(lx - bx) + abs(ly - by) - 1)