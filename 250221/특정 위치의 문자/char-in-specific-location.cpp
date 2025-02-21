#include <iostream>
using namespace std;

int main() {
    char arr[7] = "LEBROS";
    char c;
    cin>>c;
    int ans=-1;

    for(int i=0; i<=6; i++)
    if (c == arr[i])
    ans=i;

    if(ans!=-1)
    cout<<ans;
    else
    cout<<"None";
    // Please write your code here.
    return 0;
}