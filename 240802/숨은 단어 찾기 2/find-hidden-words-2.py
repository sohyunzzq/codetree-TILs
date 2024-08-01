n, m = map(int, input().split())

lst = []
for i in range(n):
    lst.append(list(input()))

cnt = 0
for i in range(n):
    for j in range(m):
        if lst[i][j] == "L":
            if j < m-2 and lst[i][j+1] == lst[i][j+2] == "E":
                cnt += 1
            if i < n-2 and lst[i+1][j] == lst[i+2][j] == "E":
                cnt += 1
            if i >= 2 and lst[i-1][j] == lst[i-2][j] == "E":
                cnt += 1
            if j >= 2 and lst[i][j-1] == lst[i][j-2] == "E":
                cnt += 1
            
            if i >= 2 and j < m-2 and lst[i-1][j+1] == lst[i-2][j+2] == "E":
                cnt += 1
            if i < n-2 and j < m-2 and lst[i+1][j+1] == lst[i+2][j+2] == "E":
                cnt += 1
            if i < n-2 and j >= 2 and lst[i+1][j-1] == lst[i+2][j-2] == "E":
                cnt += 1
            if i >= 2 and j >= 2 and lst[i-1][j-1] == lst[i-1][j-1] == "E":
                cnt += 1
print(cnt)