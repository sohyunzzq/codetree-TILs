#include <iostream>
#include <algorithm>
using namespace std;

int n;
int area[100][100];
int cnt = 0;
int max_size = 1;
bool visited[100][100];
int tmp_cnt;
int dx[4] = { -1, 0, 1, 0 };
int dy[4] = { 0, 1, 0, -1 };

bool InRange(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < n;
}

bool CanGo(int x, int y, int num) {
    return InRange(x, y) && area[x][y] == num && !visited[x][y];
}

void DFS(int x, int y) {
    int num = area[x][y];

    for (int dr = 0; dr < 4; dr++) {
        int nx = x + dx[dr];
        int ny = y + dy[dr];

        if (CanGo(nx, ny, num)) {
            tmp_cnt++;
            visited[nx][ny] = true;
            max_size = max(max_size, tmp_cnt);
            DFS(nx, ny);

        }
    }
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> area[i][j];

    for (int i=0; i<n; i++)
        for (int j = 0; j < n; j++) {
            if (!visited[i][j]) {
                visited[i][j] = true;

                tmp_cnt = 1;
                DFS(i, j);

                if (tmp_cnt >= 4)
                    cnt++;
            }
        }

    cout << cnt << " " << max_size;
    
    return 0;
}