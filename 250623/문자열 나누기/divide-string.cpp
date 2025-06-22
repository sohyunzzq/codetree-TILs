#include <iostream>
#include <string>
using namespace std;

int main() {
	int n;
	cin >> n;

	string ans;
	for (int i = 0; i < n; i++) {
		string s;
		cin >> s;

		ans += s;
	}

	for (int i = 0; i < ans.size(); i++) {
		if (i > 0 && i % 5 == 0)
			cout << endl;
		cout << ans[i];
	}
}