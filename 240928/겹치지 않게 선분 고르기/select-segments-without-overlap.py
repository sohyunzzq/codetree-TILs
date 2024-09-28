n = int(input())
line = []
for i in range(n):
    line.append(list(map(int, input().split())))

lst = []
maxi = 0
def select(index):
    global maxi
    if index == n:
        if check():
            maxi = max(maxi, len(lst))
        return
    
    lst.append(line[index])
    select(index + 1)
    lst.pop()

    select(index + 1)

def check():
    box = [0] * 1000
    for item in lst:
        for i in range(item[0], item[1]):
            if box[i] == 1:
                return False
            box[i] = 1
    
    return True

select(0)
print(maxi)