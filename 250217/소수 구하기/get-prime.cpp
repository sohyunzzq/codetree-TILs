#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;

    for(int i=2; i<=n; i++){
        int flag=1;
        for(int j=2; j<i; j++)
            if (i%j==0){
                flag=0;
                break;
            }
        if (flag)
            cout<<i<<" ";
    }
    // Please write your code here.
    return 0;
}