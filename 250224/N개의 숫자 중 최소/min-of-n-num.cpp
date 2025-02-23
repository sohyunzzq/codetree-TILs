#include <iostream>
#include <climits>

using namespace std;

int main() {
    int min_val=INT_MAX;
    int cnt=0;

    int n;
    cin>>n;
    int num[100];

    for(int i=0; i<n; i++) {
        cin>>num[i];
        if(num[i]<min_val)
        min_val=num[i];
    }

    for(int i=0; i<n; i++)
    if(num[i]==min_val)
    cnt++;

    cout<<min_val<<" "<<cnt;
    // Write your code here!

    return 0;
}
