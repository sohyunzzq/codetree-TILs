#include <iostream>
#include <queue>
using namespace std;

int n, m;
int area[200][200];
queue<pair<int, int>> q;
bool visited[200][200];
bool water[200][200];
int cnt_melt = 0;
int cnt_glacier = 0;

// 0이 물, 1이 빙하
// 바깥에서부터 들어가기?
// 물 영역을 구한 후, 따로 표시하기
// 빙하를 순회하며 표시한 물과 닿아 있으면 녹이기

int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, 1, 0, -1 };

bool InRange(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m;
}

bool CanGo(int x, int y) {
    return InRange(x, y) && area[x][y] == 0 && !visited[x][y];
}

void FindWater() {
    while (!q.empty()) {
        pair<int, int> v = q.front();
        int x = v.first;
        int y = v.second;
        q.pop();

        for (int dr = 0; dr < 4; dr++) {
            int nx = x + dx[dr];
            int ny = y + dy[dr];

            if (CanGo(nx, ny)) {
                water[nx][ny] = true;
                visited[nx][ny] = true;
                q.push({ nx, ny });
            }
        }
    }
}

void Melt() {
    cnt_melt = 0;
    for (int i=1; i<n-1; i++)
        for (int j=0; j<m; j++)
            if (area[i][j] == 1) {
                for (int dr = 0; dr < 4; dr++) {
                    int nx = i + dx[dr];
                    int ny = j + dy[dr];

                    if (InRange(nx, ny) && water[nx][ny] == true) {
                        cnt_melt++;
                        area[i][j] = 0;
                        break;
                    }
                }
            }
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            cin >> area[i][j];
            if (area[i][j] == 1)
                cnt_glacier++;
        }

    int time = 0;
    // 빙하 개수를 세놓고, 계속 뺴주기
    
    while (cnt_glacier) {
        // 현재 물을 표시하는 배열
        // visited 배열 초기화
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                water[i][j] = false;
                visited[i][j] = false;
            }

        q.push({ 0, 0 });
        water[0][0] = true;
        visited[0][0] = true;
        FindWater();

        // 현재 물을 표시해둠
        // 빙하 기준으로 돌면서, 인접한 water가 true면 녹음
        Melt();
        cnt_glacier -= cnt_melt;

        time++;
    }

    cout << time << " " << cnt_melt;
    return 0;
}