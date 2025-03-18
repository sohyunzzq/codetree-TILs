#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n, k;
vector<vector<int>> area;
vector<vector<int>> visited;
vector<vector<int>> dist;
queue<pair<int, int>> q;

int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, 1, 0, -1 };

void InitArr(vector<vector<int>>* arr, int num) {
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			(*arr)[i][j] = num;
}

bool InRange(int x, int y) {
	return 0 <= x && x < n && 0 <= y && y < n;
}

bool CanGo(int x, int y) {
	return InRange(x, y) && !visited[x][y] && area[x][y] == 1;
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
				if (dist[nx][ny] <= -1)
					dist[nx][ny] = dist[x][y] + 1;
				else
					dist[nx][ny] = min(dist[nx][ny], dist[x][y] + 1);
			}
		}
	}
}

int main() {
	cin >> n >> k;
	area.resize(n);
	visited.resize(n);
	dist.resize(n);
	for (int i = 0; i < n; i++) {
		area[i].resize(n);
		visited[i].resize(n);
		dist[i].resize(n, -1);
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> area[i][j];
		}
	}
	
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (area[i][j] == 2) {
				InitArr(&visited, 0);
				q.push({ i, j });
				visited[i][j] = 1;
				dist[i][j] = 0;

				BFS();

				for (int p=0; p<n; p++)
					for (int q = 0; q < n; q++)
						if (area[p][q] == 1 && !visited[p][q])
							dist[p][q] = -2;
			}
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++)
			cout << dist[i][j] << " ";
		cout << endl;
	}
}