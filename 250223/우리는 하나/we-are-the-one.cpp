#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int n, k, u, d;
int area[8][8];
bool visited[8][8];
int max_cnt = 0;
int cnt_city = 0;
queue<pair<int, int>> q;
bool IsPicked[8][8];
pair<int, int> picked[8 * 8];

int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, 1, 0, -1 };

bool InRange(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < n;
}

bool CanGo(int x, int y, int num) {
    return InRange(x, y) && u <= abs(num - area[x][y]) && abs(num - area[x][y]) <= d && !visited[x][y];
}

void BFS() {
    while (!q.empty()) {
        pair<int, int> v = q.front();
        int x = v.first;
        int y = v.second;
        q.pop();

        for (int dr = 0; dr < 4; dr++) {
            int nx = x + dx[dr];
            int ny = y + dy[dr];

            if (CanGo(nx, ny, area[x][y])) {
                cnt_city++;
                visited[nx][ny] = true;
                q.push({ nx, ny });
            }
        }
    }
}

void func(int curr) {
    if (curr == k) {
        // k개 뽑음, BFS 돌리기
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                visited[i][j] = false;

        cnt_city = 0;
        for (int i = 0; i < k; i++) {
            int x = picked[i].first;
            int y = picked[i].second;
            cnt_city++;

            if (!visited[x][y]) {
                q.push({ x, y });
                visited[x][y] = true;
                BFS();
            }
            max_cnt = max(max_cnt, cnt_city);
        }
        return;
    }

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (!IsPicked[i][j]) {
                picked[curr] = { i, j };
                IsPicked[i][j] = true;
                func(curr + 1);
                IsPicked[i][j] = false;
            }
}

int main() {
    cin >> n >> k >> u >> d;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> area[i][j];

    // n*n개 도시 중 k개 뽑기 -> 백트
    func(0);
    cout << max_cnt;
    return 0;
}