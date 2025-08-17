#include <iostream>
using namespace std;

#define SZ 46

int DP[SZ];

int main() {
	DP[1] = 1;
	DP[2] = 1;

	for (int i = 3; i <= SZ; i++)
		DP[i] = DP[i - 2] + DP[i - 1];

	int n;
	cin >> n;

	cout << DP[n];
}