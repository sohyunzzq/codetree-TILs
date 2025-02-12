#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;

    int num=9;
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            if (num==0)
            num=9;

            cout<<num--;
        }
        cout<<endl;
    }
    // Please write your code here.
    return 0;
}