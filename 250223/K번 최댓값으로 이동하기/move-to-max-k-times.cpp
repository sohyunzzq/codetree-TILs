#include <iostream>
#include <queue>
using namespace std;

int n, k;
int r, c;
int area[100+1][100+1];
queue<pair<int, int>> q;
bool visited[100+1][100+1];
pair<int, int> next_pos;
int max_num;

int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, 1, 0, -1 };

bool InRange(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < n;
}

bool CanGo(int x, int y, int num) {
    return InRange(x, y) && area[x][y] < num && !visited[x][y];
}

void BFS(int num) {
    while (!q.empty()) {
        pair<int, int> v = q.front();
        int x = v.first;
        int y = v.second;
        q.pop();

        for (int dr = 0; dr < 4; dr++) {
            int nx = x + dx[dr];
            int ny = y + dy[dr];

            if (CanGo(nx, ny, num)) {
                visited[nx][ny] = true;
                q.push({ nx, ny });

                if (area[nx][ny] > max_num) {
                    max_num = area[nx][ny];
                    next_pos = { nx, ny };
                }
                else if (area[nx][ny] == max_num)
                    if (nx < next_pos.first || (nx == next_pos.first && ny < next_pos.second))
                        next_pos = { nx, ny };
            }
        }
    }
}

int main() {
    cin >> n >> k;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> area[i][j];
    cin >> r >> c;
    r--, c--;

    for (int i = 0; i < k; i++) {

        for (int j = 0; j < n; j++)
            for (int m = 0; m < n; m++)
                visited[j][m] = false;

        max_num = 0;
        next_pos = { r, c };
        visited[r][c] = true;
        q.push({ r, c });
        BFS(area[r][c]);

        int nx = next_pos.first;
        int ny = next_pos.second;

        if (r == nx && c == ny)
            break;

        r = nx, c = ny;
    }

    cout << r + 1 << " " << c + 1;
    return 0;
}