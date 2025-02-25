#include <iostream>

using namespace std;

int main() {
    int n, m;
    cin>>n>>m;

    int arr[100][100];
    int num=0;

    for(int col=0; col<m; col++){
        if(col %2==0){
            for(int row=0; row<n; row++)
            arr[row][col]=num++;
        }
        else
        for(int row=n-1; row>=0; row--)
        arr[row][col]=num++;
    }

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++)
        cout<<arr[i][j]<<" ";
        cout<<endl;
    }

    // Write your code here!

    return 0;
}
