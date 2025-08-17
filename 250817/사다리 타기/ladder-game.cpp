/*
1. b를 기준으로 sort 후, swap(a, a+1) -> 원래 결과 구하기
2. 백트로 각 라인을 고를지 말지 고르기 -> 모든 경우의 수 구한 후 결과 구하기
3. 결과 동일하면 최솟값 갱신
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, m;
vector<pair<int, int>> lines;
vector<pair<int, int>> selected;
vector<int> ori_result;
vector<int> tmp_result;
int ans;

struct cmp {
	bool operator()(const pair<int, int>& a, const pair<int, int>& b) {
		return a.second < b.second;
	}
};

void GetResult(vector<pair<int, int>> lst, vector<int> &result) {
	for (int i = 0; i < lst.size(); i++) {
		pair<int, int> now = lst[i];
		int idx = now.first;

		swap(result[idx], result[idx + 1]);
	}
}

void GetAns() {
	for (int i = 1; i <= n; i++) {
		if (tmp_result[i] != ori_result[i])
			return;
	}

	ans = min(ans, int(selected.size()));
}

void func(int idx) {
	if (idx == m) {
		for (int i = 0; i <= n; i++) {
			tmp_result[i] = i;
		}

		sort(selected.begin(), selected.end(), cmp());
		GetResult(selected, tmp_result);

		GetAns();
		return;
	}

	// 현재 idx 선택
	selected.push_back(lines[idx]);
	func(idx + 1);
	selected.pop_back();

	// 현재 idx 선택 X
	func(idx + 1);
}

int main() {
	ios::sync_with_stdio(0); cin.tie(0);

	cin >> n >> m;

	ori_result.resize(n + 1);
	tmp_result.resize(n + 1);
	for (int i = 0; i <= n; i++) {
		ori_result[i] = i;
	}

	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;

		lines.push_back({ a, b });
	}

	sort(lines.begin(), lines.end(), cmp());
	GetResult(lines, ori_result);

	ans = m + 1;
	func(0);

	cout << ans;
}