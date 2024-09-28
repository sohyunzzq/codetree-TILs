n, m = map(int, input().split())

graph = []
for i in range(n + 1):
    graph.append([0] * (n + 1))

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y], graph[y][x] = 1, 1

visited = [0] * (n+1)
visited[1] = 1
ans = 0
def dfs(vertex):
    global ans
    for v in range(1, n + 1):
        if graph[vertex][v] and not visited[v]:
            visited[v] = 1
            ans += 1
            dfs(v)

dfs(1)
print(ans)