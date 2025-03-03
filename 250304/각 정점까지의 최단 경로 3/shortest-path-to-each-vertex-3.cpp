#include <iostream>
#include <queue>
#include <climits>
using namespace std;

struct Node {
	int v;
	int weight;
	bool operator<(struct Node right) const {
		return weight > right.weight;
	}
};

int n, m;
int dist[101];
bool check[101];
priority_queue<struct Node> q;

int main() {
	cin >> n >> m;

	vector<vector<int>> graph;
	graph.resize(n + 1);
	for (int i = 1; i <= n; i++)
		graph[i].resize(n + 1);

	for (int i = 0; i < m; i++) {
		int start, end, weight;
		cin >> start >> end >> weight;
		graph[start][end] = weight;
	}

	for (int i = 1; i <= n; i++) {
		dist[i] = INT_MAX;
		q.push({ i, dist[i] });
	}
	dist[1] = 0;

	while (!q.empty()) {
		struct Node now = q.top(); q.pop();
		for (int i = 1; i <= n; i++) {
			if (graph[now.v][i]) {
				if (dist[i] > dist[now.v] + graph[now.v][i]) {
					dist[i] = dist[now.v] + graph[now.v][i];
					check[i] = true;
					q.push({ i, dist[i] });
				}
			}
		}
	}

	for (int i = 2; i <= n; i++)
		if (!check[i])
			cout << -1 << endl;
		else
			cout << dist[i] << endl;
}