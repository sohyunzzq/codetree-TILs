def check(n):
    n = str(n)
    for i in n:
        if i in "369":
            return True
    return False

def game(a, b):
    cnt = 0
    for i in range(a, b+1):
        if check(i) or i % 3 == 0:
            cnt += 1
    return cnt

a, b = map(int, input().split())

print(game(a, b))