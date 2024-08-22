def row(): #ㅡ 모양
    maxi = 1
    for line in num:
        for j in range(m-2):
            maxi = max(maxi, line[j] + line[j+1] + line[j+2])

    return maxi

def col(): #ㅣ 모양
    maxi = 1
    for i in range(m):
        tmp = []
        for j in range(n):
            tmp.append(num[j][i])
        
        for j in range(n-2):
            maxi = max(maxi, tmp[j] + tmp[j+1] + tmp[j+2])
    
    return maxi

def lefttop(): #┌ 모양
    maxi = 1
    for i in range(n-1):
        for j in range(m-1):
            maxi = max(maxi, num[i][j] + num[i][j+1] + num[i+1][j])
    
    return maxi

def righttop(): #┐ 모양
    maxi = 1
    for i in range(n-1):
        for j in range(m-1):
            maxi = max(maxi, num[i][j] + num[i][j+1] + num[i+1][j+1])

    return maxi

def leftbottom(): #└ 모양
    maxi = 1
    for i in range(n-1):
        for j in range(m-1):
            maxi = max(maxi, num[i][j] + num[i+1][j] + num[i+1][j+1])
    
    return maxi

def rightbottom(): #┘ 모양
    maxi = 1
    for i in range(n-1):
        for j in range(m-1):
            maxi = max(maxi, num[i][j+1] + num[i+1][j] + num[i+1][j+1])

    return maxi

ans = 1
n, m = map(int, input().split())
num = []
for i in range(n):
    num.append(list(map(int, input().split())))

ans = max(row(), col(), lefttop(), righttop(), leftbottom(), rightbottom())

print(ans)