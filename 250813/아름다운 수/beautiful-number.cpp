#include <iostream>
#include <vector>
using namespace std;

int n;
vector<int> selected;
int cnt;

bool Check() {
	int index = 0;
	while (index < n) {
		int num = selected[index];

		// num개
		for (int i = 0; i < num; i++)
			if (index + i >= n || selected[index] != selected[index + i])
				return false;

		index += num;
	}
	return true;
}

void func(int curr) {
	if (selected.size() == n) {
		if (Check())
			cnt++;
		return;
	}

	for (int i = 1; i <= 4; i++) {
		selected.push_back(i);
		func(i + 1);
		selected.pop_back();
	}
}

int main() {
	ios::sync_with_stdio(0); cin.tie(0);

	cin >> n;

	func(0);

	cout << cnt;
}