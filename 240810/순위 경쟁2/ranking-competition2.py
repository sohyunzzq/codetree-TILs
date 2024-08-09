n = int(input())

lst = []
for i in range(n):
    a, b = input().split()
    b = int(b)
    lst.append([a, b])

a, b = 0, 0
cnt = 0
winner = ["a", "b"]

for player, score in lst:
    if player == "A":
        a += score
    else:
        b += score
    
    if a > b:
        temp = ["a"]
    elif a < b:
        temp = ["b"]
    else:
        temp = ["a", "b"]
    
    if temp != winner:
        cnt += 1
    
    winner = temp

print(cnt)