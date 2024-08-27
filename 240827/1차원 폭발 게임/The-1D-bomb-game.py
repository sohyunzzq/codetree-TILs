def get_end_index(bomb, length, start_index):
    for i in range(start_index, length):
        if bomb[start_index] != bomb[i]:
            return i-1
    
    return length - 1


def explosion(bomb):
    length = len(bomb)
    
    for start_index in range(length):
        if bomb[start_index] == 0:
            continue


        end_index = get_end_index(bomb, length, start_index)

        cnt = end_index - start_index + 1
        if cnt >= m:
            for i in range(start_index, end_index+1):
                bomb[i] = 0 

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