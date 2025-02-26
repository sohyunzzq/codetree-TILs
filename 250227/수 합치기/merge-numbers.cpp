#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    int ans = 0;
    while (arr.size() != 1) {
        sort(arr.begin(), arr.end());
        arr[0] += arr[1];
        ans += arr[0];
        arr.erase(arr.begin() + 1);
    }

    cout << ans;

    // Please write your code here.
    return 0;
}