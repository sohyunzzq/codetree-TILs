#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

bool cmp(string left, string right) {
    if (left.size() == right.size())
        for (int i = 0; i < left.size(); i++)
            if (left[i] > right[i])
                return true;
            else
                return false;
    
    string left_right = left + right;
    string right_left = right + left;

    if (stoi(left_right) > stoi(right_left))
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