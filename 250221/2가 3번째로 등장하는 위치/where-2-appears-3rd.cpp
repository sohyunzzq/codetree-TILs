#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;
    int arr[100];
    for(int i=0; i<n; i++)
    cin>>arr[i];

    int index, cnt=0;

    for(int i=0; i<n; i++){
        if (arr[i]==2)
        cnt++;

        if(cnt==3){
        cout<<i+1;
        break;
        }
    }

    // Please write your code here.
    return 0;
}