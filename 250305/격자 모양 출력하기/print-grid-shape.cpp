#include <iostream>
using namespace std;

int main() {
    int n, m;
    cin>>n>>m;

    int area[9][9]={};

    for(int i=0; i<m; i++){
        int x, y;
        cin>>x>>y;

        area[x-1][y-1]=x*y;
    }

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++)
        cout<<area[i][j]<<" ";
        cout<<endl;
    }
    // Please write your code here.
    return 0;
}