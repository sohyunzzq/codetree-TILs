#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;

    for(int col=1; col<=n; col++) {
        for(int row=0; row<n; row++){
            cout<<row*n+col<<" ";
        }
        cout<<endl;
    }
    // Please write your code here.
    return 0;
}