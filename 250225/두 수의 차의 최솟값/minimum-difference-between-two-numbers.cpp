#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;

    int ans=100;

    int arr[10];
    for(int i=0; i<n; i++)
    cin>>arr[i];

    for(int i=0; i<n; i++)
    for(int j=i+1; j<n; j++)
    if(arr[j]-arr[i]<ans)
    ans=arr[j]-arr[i];

    cout<<ans;
    // Please write your code here.
    return 0;
}