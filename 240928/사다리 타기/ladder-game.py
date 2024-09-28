#38분

#이동은 무조건 height만큼 해야 함
#고른 선에 따라서 다른 사다리가 만들어진다... 바보


def setting(line):
    ladder = []
    for i in range(height):
        ladder.append([0] * n)

    for item in line:
        ladder[item[1]-1][item[0]-1] = "A"
        ladder[item[1]-1][item[0]] = "B"
    
    return ladder

def game(ladder, numberofline):
    ans = [0] * n
    for num in range(n):
        x, y = 0, num
    
        for i in range(height):
            if ladder[x][y] == "A":
                y += 1
            elif ladder[x][y] == "B":
                y -= 1

            x += 1
        
        ans[num] = y + 1

    return ans


lst = []
def select(index):
    global mini
    if index == m:
        return

    lst.append(line[index])
    select(index + 1)

    lst.pop()

    select(index + 1)

    ladder = setting(lst)
    ans = game(ladder, len(lst))
    if ans == originalans:
        mini = min(mini, len(lst))



n, m = map(int, input().split())
line = []
for i in range(m):
    line.append(list(map(int, input().split())))

height = sorted(line, key = lambda x: -x[1])[0][1]

mini = height

ladder = setting(line)
originalans = game(ladder, height)

select(0)

print(mini)