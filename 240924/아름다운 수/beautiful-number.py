#49분
#경우의 수는 구했는데, 조건 체크하는 게 오래 걸림

#모든 경우의 수를 구한 후 체크하기?

def is_beautiful():
    index = 0
    while index < n:
        if index + lst[index] > n:
            return False
        
        for i in range(index, index + lst[index]):
            if lst[i] != lst[index]:
                return False
        
        index += lst[index]
    return True

def choose(pos):
    global cnt
    if pos == n + 1: #n자리 초과
        if is_beautiful():
            cnt += 1
        return

    for i in range(1, 5):
        lst.append(i)
        choose(pos + 1)
        lst.pop()

lst = []
cnt = 0
n = int(input())

choose(1)

print(cnt)