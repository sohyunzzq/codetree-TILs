#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n, m, h;
vector<vector<int>> area;
vector<vector<int>> visited;
vector<vector<int>> ans;
vector<vector<int>> dist;
queue<pair<int, int>> q;

int now_x, now_y;

int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, 1, 0, -1 };

void InitArr(vector<vector<int>> *arr) {
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			(*arr)[i][j] = 0;
}

bool InRange(int x, int y) {
	return 0 <= x && x < n && 0 <= y && y < n;
}

bool CanGo(int x, int y) {
	return InRange(x, y) && !visited[x][y] && area[x][y] != 1;
}

void BFS() {
	while (!q.empty()) {
		pair<int, int> now = q.front();
		q.pop();

		int x = now.first;
		int y = now.second;

		for (int dr = 0; dr < 4; dr++) {
			int nx = x + dx[dr];
			int ny = y + dy[dr];

			if (CanGo(nx, ny)) {
				visited[nx][ny] = 1;
				q.push({ nx, ny });
				dist[nx][ny] = dist[x][y] + 1;

				if (area[nx][ny] == 3) {
					ans[now_x][now_y] = dist[nx][ny];
					while (!q.empty())
						q.pop();
					return;
				}
			}
		}
	}
}

int main() {
	cin >> n >> m >> h;
	area.resize(n);
	visited.resize(n);
	ans.resize(n);
	dist.resize(n);
	for (int i = 0; i < n; i++) {
		area[i].resize(n);
		visited[i].resize(n);
		ans[i].resize(n);
		dist[i].resize(n);
	}

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			cin >> area[i][j];

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			// 2를 3으로 보내야 함
			if (area[i][j] == 2) {
				InitArr(&visited);
				InitArr(&dist);

				now_x = i, now_y = j;

				visited[i][j] = 1;
				q.push({ i, j });
				dist[i][j] = 0;
				BFS();

				if (ans[i][j] == 0)
					ans[i][j] = -1;
			}
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++)
			cout << ans[i][j] << " ";
		cout << endl;
	}
}