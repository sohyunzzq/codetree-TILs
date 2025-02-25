#include <iostream>
using namespace std;

int main() {
    int n, m;
    cin>>n>>m;

    int num=1;

    for(int i=0; i<n; i++){
    for(int j=0; j<m; j++)
    cout<<num++<<" ";
    cout<<endl;
    }
    // Please write your code here.
    return 0;
}