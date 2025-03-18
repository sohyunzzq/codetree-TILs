#include <iostream>
#include <queue>
using namespace std;

#define SZ 1000000
int n;
int num[SZ + 1];
bool visited[SZ + 1];
queue<int> q;

bool InRange(int x) {
	return 0 <= x && x <= SZ;
}

bool CanGo(int x) {
	return InRange(x) && !visited[x];
}

int main() {
	cin >> n;

	q.push(n);
	visited[n] = true;
	while (!q.empty()) {
		int now = q.front();
		q.pop();

		int cnt = num[now];

		if (CanGo(now - 1)) {
			num[now - 1] = cnt + 1;
			visited[now - 1] = true;
			q.push(now - 1);
			if (now - 1 == 1)
				break;
		}
		if (CanGo(now + 1)) {
			num[now + 1] = cnt + 1;
			visited[now + 1] = true;
			q.push(now + 1);
			if (now + 1 == 1)
				break;
		}
		if (now % 2 == 0 && CanGo(now / 2)) {
			num[now / 2] = cnt + 1;
			visited[now / 2] = true;
			q.push(now / 2);
			if (now / 2 == 1)
				break;
		}
		if (now % 3 == 0 && CanGo(now / 3)) {
			num[now / 3] = cnt + 1;
			visited[now / 3] = true;
			q.push(now / 3);
			if (now / 3 == 1)
				break;
		}
	}
	cout << num[1];
}