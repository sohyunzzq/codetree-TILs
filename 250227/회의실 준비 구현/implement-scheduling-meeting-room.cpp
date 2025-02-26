#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp(pair<int, int> left, pair<int, int> right) {
    return left.second < right.second;
}

int main() {
    int n;
    cin >> n;

    vector<pair<int, int>> arr;
    for (int i = 0; i < n; i++) {
        int s, e;
        cin >> s >> e;

        arr.push_back({ s, e });
    }

    sort(arr.begin(), arr.end(), cmp);

    int cnt = 0;
    int last = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i].first >= last) {
            cnt++;
            last = arr[i].second;
        }
    }

    cout << cnt;

    // Please write your code here.
    return 0;
}