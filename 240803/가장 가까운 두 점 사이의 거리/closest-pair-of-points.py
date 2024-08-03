import sys

def distance(coor1, coor2):
    return (coor1[0] - coor2[0]) ** 2 + (coor1[1] - coor2[1]) ** 2

n = int(input())

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

min_dis = sys.maxsize

for i in range(n):
    for j in range(i + 1, n):
        if min_dis > distance(lst[i], lst[j]):
            min_dis = distance(lst[i], lst[j])
            coor1 = lst[i]
            coor2 = lst[j]

print(min_dis)