#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Edge {
	int a, b;
	int weight;
	bool operator<(struct Edge right) const {
		return (weight < right.weight);
	}
};

int n, m;
vector<int> uf;

int Find(int a) {
	if (a == uf[a])
		return a;

	int root = Find(uf[a]);
	uf[a] = root;
	return root;
}

void Union(int a, int b) {
	int X = Find(a);
	int Y = Find(b);
	uf[X] = Y;
}

int main() {
	cin >> n >> m;
	vector<struct Edge> edges(m);
	for (int i = 0; i < m; i++) {
		int a, b, weight;
		cin >> a >> b >> weight;

		edges[i] = { a, b, weight };
	}

	sort(edges.begin(), edges.end());

	uf.resize(n + 1);
	for (int i = 1; i <= n; i++)
		uf[i] = i;

	int ans = 0;
	for (int i = 0; i < m; i++) {
		struct Edge edge = edges[i];
		if (Find(edge.a) != Find(edge.b)) {
			Union(edge.a, edge.b);
			ans += edge.weight;
		}
	}

	cout << ans;
}