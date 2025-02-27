#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

bool cmp(string left, string right) {
    string left_right = left + right;
    string right_left = right + left;

    if (stol(left_right) > stol(right_left))
        return true;
    return false;
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