#include <iostream>
using namespace std;

int main() {
    int arr[4][4];
    for(int i=0; i<4; i++)
    for(int j=0; j<4; j++)
    cin>>arr[i][j];

    for(int i=0; i<4; i++){
        int ans=0;
        for(int j=0; j<4; j++)
        ans+=arr[i][j];
        cout<<ans<<endl;
    }
    // Please write your code here.
    return 0;
}