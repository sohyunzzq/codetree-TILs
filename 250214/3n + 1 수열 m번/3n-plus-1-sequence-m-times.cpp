#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;

    for(int i=0; i<n; i++){
        int m;
        cin>>m;

        int cnt=0;
        while (m != 1){
            if (m%2==0)
            m/=2;
            else
            m=3*m+1;
            cnt++;
        }
        cout<<cnt<<endl;
    }
    // Please write your code here.
    return 0;
}