#include <iostream>
using namespace std;

int main() {
    int n, m;
    cin>>n>>m;

    int cnt=0;

    for(int i=0; i<n; i++){
        int tmp;
        cin>>tmp;

        if(m == tmp)
        cnt++;
    }

    cout<<cnt;
    // Please write your code here.
    return 0;
}