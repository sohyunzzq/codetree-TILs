#include <iostream>

using namespace std;

int main() {
    int n;
    cin>>n;
    int arr[1001]={0};

    for(int i=0; i<n; i++){
        int num;
        cin>>num;

        arr[num]++;
    }

    int ans=-1;

    for(int i=1000; i>=0; i--)
    if(arr[i]==1){
    ans=i;
    break;
    }

    cout<<ans;
    // Write your code here!

    return 0;
}
