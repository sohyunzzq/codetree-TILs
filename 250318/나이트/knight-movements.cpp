#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n;
vector<vector<int>> visited;
vector<vector<int>> dist;
queue<pair<int, int>> q;
int r1, c1, r2, c2;

int dx[] = { -1, -2, -2, -1, 1, 2, 2, 1 };
int dy[] = { -2, -1, 1, 2, 2, 1, -1, -2 };

bool InRange(int x, int y) {
	return 0 <= x && x < n && 0 <= y && y < n;
}

bool CanGo(int x, int y) {
	return InRange(x, y) && !visited[x][y];
}

void BFS() {
	while (!q.empty()) {
		pair<int, int> now = q.front();
		q.pop();

		int x = now.first;
		int y = now.second;

		for (int dr = 0; dr < 8; dr++) {
			int nx = x + dx[dr];
			int ny = y + dy[dr];

			if (CanGo(nx, ny)) {
				visited[nx][ny] = 1;
				q.push({ nx, ny });
				dist[nx][ny] = dist[x][y] + 1;

				if (nx == r2 && ny == c2) {
					while (!q.empty())
						q.pop();
					return;
				}
			}
		}
	}
}

int main() {
	cin >> n;
	visited.resize(n);
	dist.resize(n);
	for (int i = 0; i < n; i++) {
		visited[i].resize(n);
		dist[i].resize(n);
	}

	cin >> r1 >> c1 >> r2 >> c2;

	visited[r1-1][c1-1] = 1;
	q.push({ r1-1, c1-1 });
	BFS();

	if (dist[r2 - 1][c2 - 1] == 0)
		cout << -1;
	else
		cout << dist[r2 - 1][c2 - 1];
}