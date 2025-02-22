#include <iostream>
using namespace std;

int n, m;
int area[100][100];
bool ans = false;
// 오른쪽, 아래
int dx[] = { 0, 1 };
int dy[] = { 1, 0 };
bool visited[100][100] = {false,};

bool InRange(int x, int y) {
    return (0 <= x && x < n && 0 <= y && y < m);
}

bool CanGo(int x, int y) {
    return (InRange(x, y) && area[x][y] == 1 && !visited[x][y]);
}

void DFS(int x, int y) {
    if (x == n - 1 && y == m - 1) {
        ans = true;
        return;
    }

    for (int dr = 0; dr < 2; dr++) {
        int nx = x + dx[dr];
        int ny = y + dy[dr];

        if (CanGo(nx, ny)) {
            visited[nx][ny] = true;
            DFS(nx, ny);
        }
    }
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> area[i][j];

    visited[0][0] = true;
    DFS(0, 0);

    cout << ans;

    return 0;
}