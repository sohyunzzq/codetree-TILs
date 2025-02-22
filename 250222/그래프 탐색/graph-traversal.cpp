#include <iostream>
#include <vector>
using namespace std;

int n, m;
vector<bool> visited;
vector<vector<bool>> graph;
int cnt = 0;

void DFS(int v) {
    for (int curr = 1; curr<=n; curr++)
        if (graph[v][curr] && !visited[curr]) {
            cnt++;
            visited[curr] = true;
            DFS(curr);
        }
}

int main() {
    cin >> n >> m;

    visited.resize(n+1);
    for (int i = 1; i <= n; i++)
        visited[i] = false;

    graph.resize(n + 1);
    for (int i = 1; i <= n; i++)
        graph[i].resize(n + 1, false);

    for (int i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;

        graph[x][y] = true;
        graph[y][x] = true;
    }
    
    visited[1] = true;
    DFS(1);

    cout << cnt;

    return 0;
}