#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;

    int num =-n;

    for(int i=0; i<n; i++) {
        if(i%2==0){
            num+=n+1;
        for(int j=0;j<n;j++) {
            cout<<num++<<" ";
        }}
        else {
            num+=n-1;
        for(int j=0; j<n; j++) {
            cout<<num--<<" ";
        }
        }
        cout<<endl;
    }
    // Please write your code here.
    return 0;
}