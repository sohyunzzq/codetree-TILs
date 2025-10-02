#include <iostream>
#include <vector>
using namespace std;
#define endl '\n'

vector<int> uf;

int Find(int x) {
	if (uf[x] == x)
		return x;
	return uf[x] = Find(uf[x]);
}

void Union(int x, int y) {
	int X = Find(x);
	int Y = Find(y);
	
	uf[X] = Y;
}

int main() {
	ios::sync_with_stdio(0); cin.tie(0);

	int n, m;
	cin >> n >> m;

	uf.resize(n + 1);

	for (int i = 0; i <= n; i++) {
		uf[i] = i;
	}

	for (int i = 0; i < m; i++) {
		int cmd, a, b;
		cin >> cmd >> a >> b;
		
		switch (cmd) {
		case 0:
			Union(a, b);
			break;
		case 1:
			cout << (Find(a) == Find(b)) << endl;
		}
	}
}