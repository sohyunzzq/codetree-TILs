day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def check(M, D):
    if D <= day[M]:
        return True
    return False

M, D = map(int, input().split())

if check(M, D):
    print("Yes")
else:
    print("No")