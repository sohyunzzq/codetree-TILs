#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n, m;
vector<vector<int>> area;
vector<vector<int>> visited;
vector<vector<int>> dist;
queue<pair<int, int>> q;

int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, 1, 0, -1 };

bool in_range(int x, int y) {
	return 0 <= x && x < n && 0 <= y && y < m;
}

bool can_go(int x, int y) {
	return in_range(x, y) && area[x][y] != 0 && !visited[x][y];
}

void bfs() {
	while (!q.empty()) {
		pair<int, int> now = q.front();
		q.pop();

		int x = now.first;
		int y = now.second;

		for (int dr = 0; dr < 4; dr++) {
			int nx = x + dx[dr];
			int ny = y + dy[dr];

			if (can_go(nx, ny)) {
				visited[nx][ny] = 1;
				dist[nx][ny] = dist[x][y] + 1;
				q.push({ nx, ny });
			}
		}
	}
}

int main() {
	cin >> n >> m;
	area.resize(n);
	visited.resize(n);
	dist.resize(n);
	for (int i = 0; i < n; i++) {
		area[i].resize(m);
		visited[i].resize(m);
		dist[i].resize(m);
	}

	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			cin >> area[i][j];

	visited[0][0] = 1;
	q.push({ 0, 0 });
	bfs();

	if (dist[n - 1][m - 1] == 0)
		cout << -1;
	else
		cout << dist[n - 1][m - 1];
}