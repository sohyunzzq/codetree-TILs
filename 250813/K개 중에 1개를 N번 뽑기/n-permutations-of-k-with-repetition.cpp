#include <iostream>
#include <vector>
using namespace std;
#define endl '\n'

int k, n;
vector<int> selected;

void func(int index) {
	if (selected.size() == n) {
		for (int i = 0; i < n; i++)
			cout << selected[i] << " ";
		cout << endl;
		return;
	}

	for (int i = 1; i <= k; i++) {
		selected.push_back(i);
		func(index + 1);
		selected.pop_back();
	}
}

int main() {
	ios::sync_with_stdio(0); cin.tie(0);

	cin >> k >> n;

	func(1);
}