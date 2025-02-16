#include <iostream>
#include <vector>
using namespace std;

int n;
int cnt = 0;
vector<int> arr;

int Check() {
    for (int i = 0; i < arr.size();) {
        int num = arr[i];

        for (int j = i; j < i + num; j++) {
            if (j >= arr.size())
                return 0;
            if (arr[j] != num)
                return 0;
        }

        i += num;
    }
    return 1;
}

void func(int curr) {
    if (curr == n) {
        cnt += Check();
        return;
    }

    for (int i = 1; i <= 4; i++) {
        arr.push_back(i);
        func(curr + 1);
        arr.pop_back();
    }
}

int main() {
    cin >> n;
    func(0);

    cout << cnt;
    return 0;
}