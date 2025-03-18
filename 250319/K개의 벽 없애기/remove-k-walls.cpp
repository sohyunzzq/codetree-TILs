#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n, k;
int r1, c1, r2, c2;
vector<vector<int>> area;
vector<vector<int>> visited;
vector<vector<int>> tmp;
vector<vector<int>> dist;
vector<pair<int, int>> walls;
bool IsSelected[10];
vector<int> Selected;
queue<pair<int, int>> q;
int ans = 200;

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
	return InRange(x, y) && !visited[x][y] && tmp[x][y] == 0;
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

				if (nx == r2 - 1 && ny == c2 - 1) {
					while (!q.empty())
						q.pop();
					return;
				}
			}
		}
	}
}

void Copy() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			tmp[i][j] = area[i][j];
		}
	}
}

void Simulate() {
	Copy();
	InitArr(&visited);
	InitArr(&dist);

	for (int i = 0; i < k; i++) {
		pair<int, int> wall = walls[Selected[i]];
		int x = wall.first;
		int y = wall.second;

		tmp[x][y] = 0;
	}

	q.push({ r1 - 1, c1 - 1 });
	visited[r1 - 1][c1 - 1] = 1;
	dist[r1 - 1][c1 - 1] = 0;
	BFS();
	if (dist[r2 - 1][c2 - 1] != 0)
		ans = min(ans, dist[r2 - 1][c2 - 1]);
}

void func(int curr) {
	if (curr == k) {
		// k개 다 골랐음
		// 이제 빼기
		Simulate();
		return;
	}

	for (int i = 0; i < walls.size(); i++) {
		if (!IsSelected[i]) {
			IsSelected[i] = true;
			Selected.push_back(i);
			func(curr + 1);
			Selected.pop_back();
			IsSelected[i] = false;
		}
	}
}

int main() {
	cin >> n >> k;
	area.resize(n);
	visited.resize(n);
	tmp.resize(n);
	dist.resize(n);
	for (int i = 0; i < n; i++) {
		area[i].resize(n);
		visited[i].resize(n);
		tmp[i].resize(n);
		dist[i].resize(n);
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> area[i][j];
			if (area[i][j] == 1)
				walls.push_back({ i, j });
		}
	}
	cin >> r1 >> c1 >> r2 >> c2;
	func(0);

	if (ans == 200)
		cout << -1;
	else
		cout << ans;
}