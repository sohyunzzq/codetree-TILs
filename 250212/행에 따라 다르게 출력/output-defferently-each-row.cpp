#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;

    int num=0;

    for(int i=0; i<n; i++) {
        if(i%2==0)
        for(int j=0; j<n; j++) {
            cout<<++num<<" ";
        }
        else
        for(int j=0; j<n; j++) {
            num += 2;
            cout<<num<<" ";
        }
        cout<<endl;
    }
    // Please write your code here.
    return 0;
}