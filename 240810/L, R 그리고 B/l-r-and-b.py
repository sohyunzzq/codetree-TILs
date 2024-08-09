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

ans = abs(lx - bx) + abs(ly - by) - 1 #ㄱ 모양이나 ㄴ 모양으로 가기

#ㅣ 모양인데 가운데 가로막음 or  ㅡ 모양인데 가운데 가로막음
if (bx == lx and rx == bx and (ly <= ry <= by or by <= ry <= ly)) or ((by == ly and ry == by) and (bx <= rx <= lx or lx <= rx <= bx)):
    ans += 2
    
print(ans)