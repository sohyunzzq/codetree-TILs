#include <iostream>
#include <algorithm>
using namespace std;

bool cmp(string left, string right) {
    for (int i = 0; i < min(left.size(), right.size()); i++) {
        if (int(left[i] - '0') > int(right[i] - '0'))
            return true;
        else if (int(left[i] - '0') < int(right[i] - '0'))
            return false;
    }
    return (left.size() < right.size());
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