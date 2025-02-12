#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;

    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            cout << n*(i+1)-(i+1)*j<<" ";
        }
        cout<<endl;
    }
    // Please write your code here.
    return 0;
}