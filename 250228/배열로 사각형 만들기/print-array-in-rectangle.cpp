#include <iostream>
using namespace std;

int main() {
    int arr[5][5];
    for(int i=0; i<5; i++){
        for(int j=0; j<5; j++){
            if(i==0 || j==0)
            arr[i][j]=1;
            else
            arr[i][j]=arr[i-1][j]+arr[i][j-1];
        }
    }

    for(int i=0; i<5; i++){
        for(int j=0; j<5; j++)
        cout<<arr[i][j]<<" ";
        cout<<endl;
    }
    // Please write your code here.
    return 0;
}