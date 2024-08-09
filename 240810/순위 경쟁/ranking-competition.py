n = int(input())
lst = []
for i in range(n):
    a, b = input().split()
    b = int(b)
    lst.append([a, b])

winner = ["a", "b", "c"]
a, b, c = 0, 0, 0

ans = 0
for player, score in lst:
    if player == "A":
        a += score
    elif player == "B":
        b += score
    else:
        c += score
    
    if a > b and a > c:
        tmp = ["a"]
    elif b > a and b > c:
        tmp = ["b"]
    elif c > a and c > b:
        tmp = ["c"]
    elif a == b and a > c:
        tmp = ["a", "b"]
    elif b == c and c > a:
        tmp = ["b", "c"]
    elif a == c and a > b:
        tmp = ["a", "c"]
    else:
        tmp = ["a", "b", "c"]
    
    if winner != tmp:
        ans += 1
    
    winner = tmp

print(ans)