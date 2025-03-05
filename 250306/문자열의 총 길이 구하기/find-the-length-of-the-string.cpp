#include <iostream>
using namespace std;

int main() {
    int cnt=0;
    for(int i=0; i<10; i++){
        string str;
        cin>>str;
        cnt+=str.length();
    }
    cout<<cnt;
    // Please write your code here.
    return 0;
}