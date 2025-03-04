#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;

    int arr[50][50];

    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            if(i==0 || j==0)
            arr[i][j]=1;
            else
            arr[i][j]=arr[i-1][j-1]+arr[i-1][j]+arr[i][j-1];
        }
    }

    for(int i=0; i<n; i++){
    for(int j=0; j<n; j++)
    cout<<arr[i][j]<<" ";
    cout<<endl;
    }
    // Please write your code here.
    return 0;
}