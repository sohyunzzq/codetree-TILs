#include <iostream>
#include <vector>
using namespace std;

int n, m;
vector<int> uf;

int Find(int a) {
	// 내 부모가 나
	if (a == uf[a])
		return a;

	int root_node = Find(uf[a]);
	uf[a] = root_node;
	return root_node;
}

void Union(int a, int b) {
	int X = Find(a);
	int Y = Find(b);
	uf[X] = Y;
}

int main() {
	cin >> n >> m;
	uf.resize(n + 1);

	for (int i = 1; i <= n; i++)
		uf[i] = i;

	// 0이면 union
	// 1이면 find(a) == find(b) ?

	for (int i = 0; i < m; i++) {
		int cmd, a, b;
		cin >> cmd >> a >> b;

		if (cmd == 0)
			Union(a, b);
		else if (cmd == 1)
			cout << (Find(a) == Find(b)) << endl;
	}
}