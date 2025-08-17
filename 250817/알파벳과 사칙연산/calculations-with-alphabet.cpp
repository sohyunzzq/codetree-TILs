#include <iostream>
#include <vector>
#include <climits>
using namespace std;

string s;
int selected[6];
vector<int> index;
int ans = -INT_MAX;
int alpha[6];

void GetAns() {
	int tmp = selected[s[0] - 'a'];

	for (int i = 1; i < s.size(); i += 2) {
		switch (s[i]) {
		case '+':
			tmp += selected[s[i+1] - 'a'];
			break;
		case '-':
			tmp -= selected[s[i + 1] - 'a'];
			break;
		case '*':
			tmp *= selected[s[i + 1] - 'a'];
			break;
		}
	}

	ans = max(ans, tmp);
}

void func(int idx) {
	if (idx == index.size()) {
		GetAns();
		return;
	}

	for (int i = 1; i <= 4; i++) {
		selected[index[idx]] = i;
		func(idx + 1);
	}
}

int main() {
	cin >> s;

	for (int i = 0; i < s.size(); i += 2) {
		alpha[s[i] - 'a']++;
	}

	for (int i = 0; i < 6; i++) {
		if (alpha[i]) {
			index.push_back(i);
		}
	}

	func(0);

	cout << ans;
}