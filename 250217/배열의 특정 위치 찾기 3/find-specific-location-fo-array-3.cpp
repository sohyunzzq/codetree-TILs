#include <iostream>
using namespace std;

int main() {
    int arr[100];
    for(int i=0; i<100; i++){
        cin>>arr[i];

        if (arr[i]==0){
            cout << arr[i-2]+arr[i-1]+arr[i-3];
            break;
        }
    }
    // Please write your code here.
    return 0;
}