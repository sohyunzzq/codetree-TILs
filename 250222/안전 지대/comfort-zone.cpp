#include <iostream>
using namespace std;

int n, m;
int area[50][50];
bool visited[50][50];
int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, 1, 0, -1 };

// k이하는 다 가라앉음
// 안전 영역의 수가 최대가 될 때의 k, 그때의 안전 영역

bool InRange(int x, int y) {
    return (0 <= x && x < n && 0 <= y && y < m);
}

bool CanGo(int x, int y, int k) {
    return InRange(x, y) && area[x][y] > k && !visited[x][y];
}

void DFS(int x, int y, int k) {
    for (int dr = 0; dr < 4; dr++) {
        int nx = x + dx[dr];
        int ny = y + dy[dr];

        if (CanGo(nx, ny, k)) {
            visited[nx][ny] = true;
            DFS(nx, ny, k);
        }
    }
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> area[i][j];

    int min_k = 100, max_k = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            min_k = min(min_k, area[i][j]);
            max_k = max(max_k, area[i][j]);
        }

    int ans = 1;
    int safe_zone = 0;

    for (int k = max(1, min_k-1); k <= max_k; k++) {
        int cnt = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                visited[i][j] = false;

        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                if (area[i][j] > k && !visited[i][j]) {
                    visited[i][j] = true;
                    cnt++;
                    DFS(i, j, k);
                }
            }

        if (cnt > safe_zone) {
            safe_zone = cnt;
            ans = k;
        }
    }

    cout << ans << " " << safe_zone;
    return 0;
}