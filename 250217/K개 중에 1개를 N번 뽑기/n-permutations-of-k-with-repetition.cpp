#include <iostream>
#include <vector>
using namespace std;

int n, k;

vector<int> arr;

void func(int curr) {
    if (curr == n) {
        for (int i=0; i<n; i++)
            cout << arr[i] << " ";
        cout << endl;
        return;
    }

    for (int i=1; i<=k; i++){
        arr.push_back(i);
        func(curr+1);
        arr.pop_back();
    }
}

int main() {
    cin>>k>>n;
    func(0);
    // Please write your code here.
    return 0;
}