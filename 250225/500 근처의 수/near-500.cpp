#include <iostream>
using namespace std;

int main() {
    int arr[10];
    for(int i=0; i<10; i++)
    cin>>arr[i];

    int min_val=1000;
    int max_val=0;

    for(int i=0; i<10; i++){
        if (arr[i]<500 && arr[i]>max_val)
        max_val=arr[i];
        
        if(arr[i]>500 && arr[i]<min_val)
        min_val=arr[i];
    }

    cout<<max_val<<" "<<min_val;
    // Please write your code here.
    return 0;
}