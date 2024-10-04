import sys

string = input()

alphas = set()

for i in range(len(string)):
    if i % 2 == 0:
        alphas.add(string[i])

alphas = list(alphas)
lst = []
matched = {}

maxi = -sys.maxsize

def get_value():
    ans = matched[string[0]]

    for i in range(1, len(string), 2):
        oper = string[i]
        alpha = matched[string[i + 1]]

        if oper == "+":
            ans += alpha
        elif oper == "-":
            ans -= alpha
        else:
            ans *= alpha
    
    return ans

def assign():
    for i in range(len(alphas)):
        matched[alphas[i]] = lst[i]

def choose(pos):
    global maxi

    if pos == len(alphas):
        assign()
        maxi = max(maxi, get_value())
        return

    for i in range(1, 5):
        lst.append(i)
        choose(pos + 1)
        lst.pop()

choose(0)
print(maxi)