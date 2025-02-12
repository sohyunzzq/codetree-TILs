#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;

    for(int row=0; row<n; row++){
        for(int col=0; col<n; col++){
            
            cout<<10+row*2+1+col*2+1-1<<" ";
        }
        cout<<endl;
    }
    // Please write your code here.
    return 0;
}