#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin>>a>>b;

    for(int i=2; i<=8; i+=2) {
        for(int j=b; j>=a; j--) {
            cout<<j<<" * "<<i<<" = "<<j*i;
            if(j==a)
            cout<<endl;
            else
            cout<<" / ";
        }
    }
    // Please write your code here.
    return 0;
}