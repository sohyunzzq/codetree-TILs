#include <iostream>
using namespace std;

int main() {
	string s;
	cin >> s;

	bool ee = false;
	bool ab = false;

	for (int i = 0; i < s.size() - 2; i++) {
		if (s.size() < 2)
			break;

		if (s[i] == 'e' && s[i + 1] == 'e')
			ee = true;

		if (s[i] == 'a' && s[i + 1] == 'b')
			ab = true;
	}

	if (ee)
		cout << "Yes ";
	else
		cout << "No ";

	if (ab)
		cout << "Yes";
	else
		cout << "No";
}