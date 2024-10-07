n = int(input())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))

def get_cnt(x, y):
    cnt = 0
    for row in range(x, x + 3):
        cnt += sum(area[row][y:y+3])
    
    return cnt

maxi = 0
for row in range(n-3+1):
    for col in range(n-3+1):
        maxi = max(maxi, get_cnt(row, col))

print(maxi)