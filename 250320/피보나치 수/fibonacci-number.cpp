#include <iostream>
#include <vector>
using namespace std;

vector<int> DP;

int GetDP(int num) {
	if (num <= 2)
		return 1;

	if (DP[num] != -1)
		return DP[num];

	if (DP[num - 1] == -1)
		DP[num - 1] = GetDP(num - 1);

	if (DP[num - 2] == -1)
		DP[num - 2] = GetDP(num - 2);

	return DP[num - 1] + DP[num - 2];
}

int main() {
	int n;
	cin >> n;

	DP.resize(n + 1, -1);
	DP[n] = GetDP(n);

	cout << DP[n];
}