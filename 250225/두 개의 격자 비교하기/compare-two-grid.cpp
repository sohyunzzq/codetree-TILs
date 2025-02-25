#include <iostream>
using namespace std;

int main() {
    int n, m;
    cin>>n>>m;

    int arr1[10][10];
    int arr2[10][10];
    int check[10][10]={};

    for(int i=0; i<n; i++)
    for(int j=0; j<m; j++)
    cin>>arr1[i][j];

    for(int i=0; i<n; i++)
    for(int j=0; j<m; j++)
    cin>>arr2[i][j];

    for(int i=0; i<n; i++)
    for(int j=0; j<m; j++)
    check[i][j]=(arr1[i][j]!=arr2[i][j]);

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++)
        cout<<check[i][j]<<" ";
        cout<<endl;
    }

    // Please write your code here.
    return 0;
}