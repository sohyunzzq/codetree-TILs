#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;
    char a='Z';

    for(int i=0; i<n; i++) {
        for(int j=0; j<=i; j++) {
            if (a=='Z')
            a='A';
            cout<<a++;
        }
        cout<<endl;
    }
    // Please write your code here.
    return 0;
}