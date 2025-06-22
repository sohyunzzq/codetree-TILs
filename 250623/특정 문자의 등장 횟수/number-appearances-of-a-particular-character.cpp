#include <iostream>
using namespace std;

int main() {
	string s;
	cin >> s;

	int ee = 0;
	int eb = 0;

	for (int i = 0; i < s.size() - 1; i++) {
		if (s.size() < 2)
			break;

		if (s[i] == 'e' && s[i + 1] == 'e')
			ee++;
		else if (s[i] == 'e' && s[i + 1] == 'b')
			eb++;
	}

	cout << ee << " " << eb;
}