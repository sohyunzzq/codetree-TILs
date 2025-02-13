#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;

    for(int i=0; i<n; i++) {
        int tmp=n-i;
        for(int j=0; j<i; j++)
        cout<<"  ";
        for(int j=0; j<n-i; j++)
        cout<<tmp--<<" ";
        cout<<endl;
    }
    // Please write your code here.
    return 0;
}