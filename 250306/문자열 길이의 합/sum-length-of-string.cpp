#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;
    int len=0;
    int cnt=0;
    for(int i=0; i<n; i++){
        string str;
        cin>>str;

        len+=str.length();
        if(str[0]=='a')
        cnt++;
    }

    cout<<len<<" "<<cnt;
    // Please write your code here.
    return 0;
}