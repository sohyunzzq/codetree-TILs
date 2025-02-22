#include <iostream>
#include <queue>
using namespace std;

int n, m;
int area[100][100];
queue<pair<int, int>> q;
bool visited[100][100];
int ans = 0;

int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, 1, 0, -1 };

bool InRange(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m;
}

bool CanGo(int x, int y) {
    return InRange(x, y) && area[x][y] == 1 && !visited[x][y];
}

void BFS() {
    while (!q.empty()) {
        pair<int, int> v = q.front();
        int x = v.first, y = v.second;
        q.pop();

        for (int dr = 0; dr < 4; dr++) {
            int nx = x + dx[dr];
            int ny = y + dy[dr];

            if (nx == n - 1 && ny == m - 1) {
                ans = 1;
                return;
            }

            if (CanGo(nx, ny)) {
                visited[nx][ny] = true;
                q.push({ nx, ny });
            }
        }
    }
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> area[i][j];

    q.push({ 0, 0 });
    BFS();

    cout << ans;
    return 0;
}