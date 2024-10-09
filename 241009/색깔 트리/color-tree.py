class NODE:
    def __init__(self, mid, p, color, depth):
        self.mid = mid
        self.p = p
        self.color = color
        self.depth = depth

def get_depth(vertex, count):
    global maxi
    maxi = max(maxi, count)

    visited[vertex] = 1
    for v in graph[vertex]:
        if not visited[v]:
            visited[v] = 1
            get_depth(v, count + 1)

    visited[vertex] = 0
    return maxi

maxi = 0
visited = [0] * 100001
def POSSIBLE():
    global maxi
    global visited
    for v in overall:
        visited = [0] * 100001
        maxi = 0
        max_depth = get_depth(v.mid, 1)

        if max_depth > v.depth: #하나를 더해야 node를 추가했을 때를 가정할 수 있음
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
    global visited
    visited[root] = 1

    for v in overall:
        if v.p == root:
            v.color = col
            visited[v.mid] = 1
            change_sub(v.mid, col)

def CHANGE_COLOR():
    global visited
    root = cmd[1]
    col = cmd[2]

    visited = [0] * 100001

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
    global visited

    for v in overall:
        if v.mid in graph[vertex.mid] and not visited[v.mid]:
            kindofcolor.add(v.color)
            if len(kindofcolor) == 5:
                return 5
            visited[v.mid] = 1
            get_color(v, kindofcolor)

    return len(kindofcolor)

def PRINT_SCORE():
    global visited
    ans = 0

    for v in overall:
        visited = [0] * 100001
        kindofcolor = set()
        kindofcolor.add(v.color)
        visited[v.mid] = 1

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