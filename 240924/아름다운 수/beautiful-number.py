#n자리 아름다운 수 구하기
#모든 경우의 수를 구한 후 체크하기?

def is_beautiful():
    number = lst[0]
    cnt = 1
    for i in range(n - 1):
        if cnt == number:
            cnt = 1
            number = lst[i+1]

        elif lst[i] != lst[i+1]:
            if cnt != number:
                return False
            number = lst[i+1]
            cnt = 1
        else:
            cnt += 1
    
    if number != cnt:
        return False
    
    return True

def choose(pos):
    global cnt
    if pos == n + 1: #n자리 초과
        if is_beautiful():
            ans.append(lst)
        return

    for i in range(1, 5):
        lst.append(i)
        choose(pos + 1)
        lst.pop()

lst = []
ans = []
n = int(input())

choose(1)

print(len(ans))