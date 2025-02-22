#include <iostream>
#include <queue>
using namespace std;

int n, k;
int ans = 0;
int area[100][100];
bool visited[100][100];
queue<pair<int, int>> q;

int dx[] = { -1, 0,1,0 };
int dy[] = { 0,1,0,-1 };

bool InRange(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < n;
}

bool CanGo(int x, int y) {
    return InRange(x, y) && area[x][y] == 0 && !visited[x][y];
}

void BFS() {
    while (!q.empty()) {
        pair<int, int> v = q.front();
        int x = v.first, y = v.second;
        q.pop();

        for (int dr = 0; dr < 4; dr++) {
            int nx = x + dx[dr];
            int ny = y + dy[dr];

            if (CanGo(nx, ny)) {
                ans++;
                q.push({ nx, ny });
                visited[nx][ny] = true;
            }
        }
    }
}

int main() {
    cin >> n >> k;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> area[i][j];

    for (int i = 0; i < k; i++) {
        int x, y;
        cin >> x >> y;

        if (!visited[x - 1][y - 1]) {
            ans++;
            q.push({ x - 1, y - 1 });
            visited[x - 1][y - 1] = true;
            BFS();
        }
    }

    cout << ans;
    return 0;
}