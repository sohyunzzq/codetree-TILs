#include <iostream>
using namespace std;

int main() {
    int arr[2][4];
    for(int i=0; i<2; i++)
    for(int j=0; j<4; j++)
    cin>>arr[i][j];

    cout<<fixed;
    cout.precision(1);

    double total=0;
    for(int i=0; i<2; i++){
        double sum=0;
        for(int j=0; j<4; j++)
        sum+=arr[i][j];
        cout<<sum/4<<" ";
    }
    cout<<endl;

    for(int i=0; i<4; i++){
        double sum=0;
        for(int j=0; j<2; j++){
        total+=arr[j][i];
        sum+=arr[j][i];
        }
        cout<<sum/2<<" ";
    }

    cout<<endl;

    cout<<total/8;
    // Please write your code here.
    return 0;
}