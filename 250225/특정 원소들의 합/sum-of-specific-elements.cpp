#include <iostream>
using namespace std;

int main() {
    int area[4][4];
    for(int i=0; i<4;i++)
    for(int j=0; j<4; j++)
    cin>>area[i][j];

    int sum=0;

    for(int row=0; row<4; row++)
    for(int col=0; col<=row; col++)
    sum+=area[row][col];

    cout<<sum;

    // Please write your code here.
    return 0;
}