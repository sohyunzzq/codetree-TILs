#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;

    int num=2;

    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            if (num == 10)
            num=2;

            cout<<num<<" ";
            num+=2;
        }
        cout<<endl;
    }
    // Please write your code here.
    return 0;
}