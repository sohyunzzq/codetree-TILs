#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;

    int arr[10][10];
    int num=1;
    
    for(int col=0; col<n; col++){
        if(col % 2 == 0)
        for(int row=n-1; row>=0; row--){
            arr[row][n-col-1]=num++;
         
        }
        else{
        for(int row=0; row<n; row++)
        arr[row][n-col-1]=num++;
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