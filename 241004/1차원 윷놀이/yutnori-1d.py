n, m, k = map(int, input().split())
yut = list(map(int, input().split()))

maxi = 0
lst = []

def get_score():
    ans = 0

    score = [0] * (k + 1)

    for i in range(n):
        score[lst[i]] += yut[i]
    
    for item in score:
        if item >= m:
            ans += 1
    
    return ans

def choose(pos):
    global maxi

    if pos == n:
        maxi = max(maxi, get_score())
        return
    
    for i in range(1, k + 1):
        lst.append(i)
        choose(pos + 1)
        lst.pop()

choose(0)
print(maxi)