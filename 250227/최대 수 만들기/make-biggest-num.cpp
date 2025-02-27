#include <iostream>
#include <algorithm>
using namespace std;

bool cmp(string left, string right) {
    int min_len = min(left.size(), right.size());
    for (int i = 0; i < min_len; i++) {
        if (int(left[i] - '0') >= int(right[i] - '0'))
            return true;
        else if (int(left[i] - '0') < int(right[i] - '0'))
            return false;
    }
    if (left.size() < right.size()) {
        if (right[min_len] > right[0])
            return true;
        else
            return false;
    }
    if (left.size() > right.size()) {
        if (left[min_len] > left[0])
            return true;
        else
            return false;
    }
}

int main() {
    int n;
    cin >> n;
    string nums[50000];
    for (int i = 0; i < n; i++)
        cin >> nums[i];

    sort(nums, nums + n, cmp);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < nums[i].size(); j++)
            cout << nums[i][j];

    return 0;
}