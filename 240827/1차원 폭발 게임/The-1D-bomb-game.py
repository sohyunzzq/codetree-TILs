def explosion(bomb):
    length = len(bomb)
    
    for i in range(length):
        cnt = 0
        if bomb[i] == 0:
            continue
        for j in range(i, length):
            if bomb[i] != bomb[j]:
                if cnt >= m:
                    for k in range(i, j):
                        bomb[k] = 0
                break
            
            cnt += 1
            if bomb[i] == bomb[j] and j == length - 1:
                if cnt >= m:
                    for k in range(i, j+1):
                        bomb[k] = 0
            
    return bomb
        
def pull(bomb):
    length = len(bomb)

    temp = []
    
    for i in range(length):
        if bomb[i] != 0:
            temp.append(bomb[i])
    
    return temp


n, m = map(int, input().split())
bomb = []
for i in range(n):
    bomb.append(int(input()))

while True:
    ex = explosion(bomb)
    pu = pull(ex)

    if bomb == pu:
        break
    
    bomb = pu


print(len(bomb))
for item in bomb:
    print(item)