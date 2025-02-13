#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;

    for(int i=0; i<n; i++){
        for(int j=n-i; j<=n; j++)
        cout<<j<<" ";
        cout<<endl;
    }
    // Please write your code here.
    return 0;
}