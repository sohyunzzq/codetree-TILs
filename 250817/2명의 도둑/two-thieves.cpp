#include <iostream>
#include <vector>
using namespace std;

#define N_SZ 11

int n, m, c;
int weight[N_SZ][N_SZ];
int sum[N_SZ][N_SZ];
vector<int> arr;
vector<int> selected;
int ret;
int ans;

void func(int idx) {
	if (idx == m) {
		int c_sum = 0;
		int sq_sum = 0;
		for (int i = 0; i < selected.size(); i++) {
			c_sum += selected[i];
			sq_sum += selected[i] * selected[i];

			if (c_sum > c)
				return;
		}

		ret = max(ret, sq_sum);
		return;
	}

	// 현재 idx 선택
	selected.push_back(arr[idx]);
	func(idx + 1);
	selected.pop_back();

	// 현재 idx 선택 X
	func(idx + 1);
}

void FillSum() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= n - m; j++) {
			// i행 j열부터 m개 고르기
			arr.clear();
			for (int k = 0; k < m; k++)
				arr.push_back(weight[i][j + k]);

			ret = 0;
			func(0);

			sum[i][j] = ret;
 		}
	}
}

void GetAns() {
	int M = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			M = sum[i][j];

			for (int a = 0; a < n; a++) {
				// 같은 행이면
				if (i == a) {
					int st = j + m;

					for (st; st < n; st++) {
						ans = max(ans, M + sum[a][st]);
					}
				}
				else {
					for (int b = 0; b < n; b++) {
						ans = max(ans, M + sum[a][b]);
					}
				}
			}
		}
	}
}

int main() {
	cin >> n >> m >> c;
	
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> weight[i][j];
		}
	}
	
	FillSum();
	
	// sum 배열에서 안 겹치게 2개 고르기
	GetAns();

	cout << ans;
}