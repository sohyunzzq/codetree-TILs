#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int n, k, m;
int area[100][100];
int ans = 0;
int stone_cnt = 0;
pair<int, int> stone[100 * 100];
pair<int, int> picked[8];
int temp[100][100];
queue<pair<int, int>> q;
pair<int, int> coords[100 * 100];
bool visited[100][100];
int cnt = 0;

int dx[4] = { -1, 0, 1, 0 };
int dy[4] = { 0, 1, 0, -1 };

bool InRange(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < n;
}

bool CanGo(int x, int y) {
    return InRange(x, y) && temp[x][y] == 0 && !visited[x][y];
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

            if (CanGo(nx, ny)) {
                q.push({ nx, ny });
                cnt++;
                visited[nx][ny] = true;
            }
        }
    }
}

void Clear() {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            temp[i][j] = area[i][j];

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            visited[i][j] = false;
    
    // 선택한 돌의 개수만큼 치우기
    for (int i = 0; i < m; i++)
        temp[picked[i].first][picked[i].second] = 0;

    // 돌 치운 후 BFS 돌려서 개수 찾기
    cnt = 0;
    for (int i = 0; i < k; i++) {
        int x = coords[i].first;
        int y = coords[i].second;

        if (!visited[x][y]) {
            q.push({ x, y });
            cnt++;
            visited[x][y] = true;
            BFS();
        }
    }
    ans = max(ans, cnt);
}

void func(int curr) {
    if (curr == m) {
        // m개 뽑았음 -> temp에서 지우고 BFS
        Clear();
        return;
    }

    for (int i = 0; i < stone_cnt; i++) {
        picked[curr] = stone[i];
        func(curr + 1);
        picked[curr] = { -1, -1 };
    }
}

int main() {
    cin >> n >> k >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            cin >> area[i][j];
            if (area[i][j])
                stone[stone_cnt++] = { i,j };
        }
    
    // 돌의 위치 저장 후 완탐?
    // 모든 돌의 위치를 저장한 후,
    // area를 복제한 temp 배열에서 m개 지운 후 그때마다 BFS
    
    // stone_cnt개 중 m개를 뽑기

    for (int i = 0; i < k; i++) {
        int x, y;
        cin >> x >> y;
        coords[i] = { x-1, y-1 };
    }

    func(0);

    cout << ans;

    return 0;
}