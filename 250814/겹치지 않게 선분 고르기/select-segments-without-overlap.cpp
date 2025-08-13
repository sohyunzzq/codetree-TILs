#include <iostream>
#include <vector>
using namespace std;

#define SZ 1000

int n;
vector<pair<int, int>> lines;
vector<int> selected;
bool check[SZ];
int ans;

bool Possible(pair<int, int> now) {
	int st = now.first;
	int en = now.second;

	for (int i = st; i < en; i++) {
		if (check[i])
			return false;
	}
	return true;
}

void Draw(pair<int, int> now) {
	int st = now.first;
	int en = now.second;

	for (int i = st; i < en; i++)
		check[i] = true;
}

void Erase(pair<int, int> now) {
	int st = now.first;
	int en = now.second;

	for (int i = st; i < en; i++)
		check[i] = false;
}

void func(int index, int cnt) {
	if (index > n)
		return;

	ans = max(ans, cnt);

	for (int i = index; i < n; i++) {
		pair<int, int> now = lines[i];

		if (Possible(now)) {
			Draw(now);
			func(index + 1, cnt + 1);

			Erase(now);
		}
		func(index + 1, cnt);
	}
}

int main() {
	ios::sync_with_stdio(0); cin.tie(0);

	cin >> n;

	for (int i = 0; i < n; i++) {
		int a, b;
		cin >> a >> b;

		lines.push_back({ a, b });
	}

	func(0, 0);

	cout << ans;
}