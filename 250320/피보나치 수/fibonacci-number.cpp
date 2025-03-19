#include <iostream>
#include <vector>
using namespace std;

vector<int> DP;

int GetDP(int num) {
	if (num <= 2)
		return DP[num] = 1;

	if (DP[num] != -1)
		return DP[num];

	return DP[num] = GetDP(num - 1) + GetDP(num - 2);
}

int main() {
	int n;
	cin >> n;

	DP.resize(n + 1, -1);
	cout << GetDP(n);
}