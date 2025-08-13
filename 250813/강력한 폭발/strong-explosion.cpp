#include <iostream>
#include <vector>
using namespace std;

int n;
vector<vector<int>> area;
vector<vector<int>> temp;
vector<pair<int, int>> bomb;
vector<int> selected;
int ans;

void CopyArr(vector<vector<int>> *dst, vector<vector<int>> *src) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			(*dst)[i][j] = (*src)[i][j];
		}
	}
}

bool InRange(int x, int y) {
	return 0 <= x && x < n && 0 <= y && y < n;
}

int GetCnt() {
	int cnt = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (temp[i][j] > 0)
				cnt++;
		}
	}
	return cnt;
}

void Simulation() {
	CopyArr(&temp, &area);

	for (int i = 0; i < bomb.size(); i++) {
		pair<int, int> now = bomb[i];
		int x = now.first;
		int y = now.second;

		if (selected[i] == 1) {
			for (int i = -2; i <= 2; i++) {
				if (InRange(x + i, y))
					temp[x + i][y] = 2;
			}
		}
		else if (selected[i] == 2) {
			int dx[4] = { 1, 0, -1, 0 };
			int dy[4] = { 0, 1, 0, -1 };

			for (int dr = 0; dr < 4; dr++) {
				int nx = x + dx[dr];
				int ny = y + dy[dr];

				if (InRange(nx, ny))
					temp[nx][ny] = 2;
			}
		}
		else if (selected[i] == 3) {
			int dx[4] = { -1, -1, 1, 1 };
			int dy[4] = { -1, 1, 1, -1 };

			for (int dr = 0; dr < 4; dr++) {
				int nx = x + dx[dr];
				int ny = y + dy[dr];
				
				if (InRange(nx, ny))
					temp[nx][ny] = 2;
			}
		}
	}

	ans = max(ans, GetCnt());
}

void func(int curr) {
	if (curr == bomb.size()){
		Simulation();
		return;
	}

	for (int i = 1; i <= 3; i++) {
		selected.push_back(i);
		func(curr + 1);
		selected.pop_back();
	}
}

int main() {
	ios::sync_with_stdio(0); cin.tie(0);

	cin >> n;
	area.resize(n);
	temp.resize(n);
	for (int i = 0; i < n; i++) {
		area[i].resize(n);
		temp[i].resize(n);
	}

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++) {
			cin >> area[i][j];
			if (area[i][j] == 1)
				bomb.push_back({ i, j });
		}

	func(0);

	cout << ans;
}