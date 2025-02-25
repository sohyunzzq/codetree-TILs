#include <iostream>

using namespace std;

int main() {
    int n;
    cin>>n;

    int ans=0;

    int arr[1000];

    for(int i=0; i<n; i++)
    cin>>arr[i];

    for(int i=0; i<n; i++)
    for(int j=i+1; j<n; j++)
    if(ans<arr[j]-arr[i])
    ans=arr[j]-arr[i];

    cout<<ans;
    // Write your code here!

    return 0;
}
