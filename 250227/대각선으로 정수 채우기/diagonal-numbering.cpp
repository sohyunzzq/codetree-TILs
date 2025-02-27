#include <iostream>

using namespace std;

int n, m;

int main() {
    cin >> n >> m;
    int arr[100][100];

    int num=1;

    for(int row=0; row<n; row++){
        for(int col=0; col<m; col++){
            if(arr[row][col]==0){
            int j=row;
            for(int i=col; i>=0 && j<n; i--){
                arr[j++][i]=num++;
            }
            }
        }
    }

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++)
        cout<<arr[i][j]<<" ";
        cout<<endl;
    }

    // Please write your code here.

    return 0;
}
