#include <iostream>
using namespace std;

int main() {
    int n, k;
    cin>>n>>k;

    int coins[10];
    for (int i=0; i<n; i++)
        cin>>coins[i];
    
    int cnt=0;
    for (int i=n-1; i>=0; i--) {
        cnt += k / coins[i];
        k %= coins[i];
    }

    cout<<cnt;
    // Please write your code here.
    return 0;
}