#38분

#사다리 타기 알고리즘
#라인들을 위에서부터 오도록 정렬하고
#가로선을 만나면 그거에 해당하는 값만 swap하면 된다

lst = []
def select(index):
    global mini

    if index == m:
        if game():
            mini = min(mini, len(lst))
        return

    lst.append(line[index])
    select(index + 1)
    lst.pop()

    select(index + 1)


def game():
    originalans = [0] * n
    ans = [0] * n

    for i in range(1, n + 1):
        originalans[i-1] = i 
    for i in range(1, n + 1):
        ans[i-1] = i

    for item in line:
        originalans[item[0] - 1], originalans[item[0]] = originalans[item[0]], originalans[item[0] - 1]
    
    for item in lst:
        ans[item[0] - 1], ans[item[0]] = ans[item[0]], ans[item[0] - 1]

    if originalans == ans:
        return True
    return False


n, m = map(int, input().split())
line = []
for i in range(m):
    line.append(list(map(int, input().split())))
line.sort(key = lambda x: x[1])

mini = m
select(0)

print(mini)