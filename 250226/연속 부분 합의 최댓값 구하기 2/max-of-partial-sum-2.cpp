#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> num(n);
    for (int i = 0; i < n; i++)
        cin >> num[i];

    int max_val = -1000;
    int tmp_sum = 0;
    for (int i = 0; i < n; i++) {
        tmp_sum += num[i];
        max_val = max(max_val, tmp_sum);
        if (tmp_sum < 0) {
            tmp_sum = 0;
        }
    }

    cout << max_val;
    // Please write your code here.
    return 0;
}