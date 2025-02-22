#include <iostream>
#include <algorithm>
using namespace std;

#define endl '\n';

int n;
int area[25][25];
int village = 0;
int people[25] = {};
bool visited[25][25];

int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, 1, 0, -1 };

bool InRange(int x, int y) {
    return (0 <= x && x < n && 0 <= y && y < n);
}

bool CanGo(int x, int y) {
    return (InRange(x, y) && area[x][y] == 1 && !visited[x][y]);
}

void DFS(int x, int y, int village) {
    for (int dr = 0; dr < 4; dr++) {
        int nx = x + dx[dr];
        int ny = y + dy[dr];

        if (CanGo(nx, ny)) {
            people[village]++;
            visited[nx][ny] = true;
            DFS(nx, ny, village);
        }
    }
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> area[i][j];

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            if (area[i][j] && !visited[i][j]) {
                people[village]++;
                visited[i][j] = true;
                DFS(i, j, village);
                village++;
            }
        }

    sort(people, people+village);
    cout << village << endl;
    for (int i = 0; i < village; i++)
        cout << people[i] << endl;
    return 0;
}