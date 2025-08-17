#include <iostream>
using namespace std;

#define SZ 1001

int DP[SZ];

int main() {
	ios::sync_with_stdio(0); cin.tie(0);
	int n;
	cin >> n;

	DP[0] = DP[1] = 0;
	DP[2] = DP[3] = 1;
	DP[4] = 1;
	DP[5] = 2;

	for (int i = 6; i <= n; i++) {
		for (int j = i - 2; j > i / 2; j--) {
			DP[i] += (DP[j] * DP[i - j]) % 10007;
		}
	}

	cout << DP[n];
}