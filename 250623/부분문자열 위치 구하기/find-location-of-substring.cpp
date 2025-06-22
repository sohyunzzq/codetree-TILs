#include <iostream>
using namespace std;

int main() {
	string s, target;
	cin >> s >> target;

	int ans = -1;
	for (int i = 0; i < s.size() - target.size(); i++) {
		if (ans != -1)
			break;
		for (int j = 0; j < target.size(); j++) {
			if (s[i + j] != target[j])
				break;
			ans = i;
			break;
		}
	}

	cout << ans;
}