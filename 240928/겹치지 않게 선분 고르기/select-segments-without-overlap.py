n = int(input())
line = []
for i in range(n):
    line.append(list(map(int, input().split())))

lst = []
maxi = 0

def select(pos):
    global maxi
    if pos == n:
        return

    for i in range(n):
        lst.append(line[i])
        if check():
            maxi = max(maxi, len(lst))
        select(pos + 1)
        lst.pop()

def check():
    lst.sort(key = lambda x: x[0])
    
    for i in range(1, len(lst)):
        if lst[i][0] <= lst[i-1][1]:
            return False
    
    return True

select(0)

print(maxi)