import sys
sys.stdin = open("input.txt", "r")

class NODE:
    def __init__(self, mid, p, color, depth):
        self.mid = mid
        self.p = p
        self.color = color
        self.depth = depth

def get_depth(vertex, count):
    global maxi
    maxi = max(maxi, count)

    for v in graph[vertex]:
        get_depth(v, count + 1)

    return maxi

maxi = 0
def POSSIBLE():
    global maxi
    for v in overall:
        maxi = 0
        max_depth = get_depth(v.mid, 1)

        if max_depth > v.depth:
            return False

    return True

def ADD_NODE():
    node = NODE(cmd[1], cmd[2], cmd[3], cmd[4])
    if node.p == -1:
        overall.append(node)
        return

    overall.append(node)
    graph[node.p].append(node.mid)

    if not POSSIBLE():
        graph[node.p].remove(node.mid)
        overall.pop()

def change_sub(root, col):
    for v in overall:
        if v.p == root:
            v.color = col
            change_sub(v.mid, col)

def CHANGE_COLOR():
    root = cmd[1]
    col = cmd[2]

    for v in overall:
        if v.mid == root:
            v.color = col

    change_sub(root, col)

def PRINT_COLOR():
    num = cmd[1]

    for v in overall:
        if v.mid == num:
            print(v.color)
            return

def get_color(vertex, kindofcolor):
    for v in overall:
        if v.mid in graph[vertex.mid]:
            kindofcolor.add(v.color)
            if len(kindofcolor) == 5:
                return 5
            get_color(v, kindofcolor)

    return len(kindofcolor)

def PRINT_SCORE():
    ans = 0

    for v in overall:
        kindofcolor = set()
        kindofcolor.add(v.color)

        ans += get_color(v, kindofcolor) ** 2

    print(ans)

Q = int(input())

graph = []
for i in range(100000 + 1):
    graph.append([])

overall = []
for _ in range(Q):
    cmd = list(map(int, input().split()))

    if cmd[0] == 100:
        ADD_NODE()
    elif cmd[0] == 200:
        CHANGE_COLOR()
    elif cmd[0] == 300:
        PRINT_COLOR()
    elif cmd[0] == 400:
        PRINT_SCORE()