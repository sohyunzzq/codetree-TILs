#include <iostream>
#include <climits>
#include <algorithm>
using namespace std;

int main() {
    int min_len=INT_MAX;
    int max_len=0;
    for(int i=0; i<3; i++){
        string str;
        cin>>str;

        min_len=min(min_len, int(str.length()));
        max_len=max(max_len, int(str.length()));
    }

    cout<<max_len-min_len;
    // Please write your code here.
    return 0;
}