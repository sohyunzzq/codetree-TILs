#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;
    char a='A';

    for(int i=0; i<n; i++){
        for(int j=0; j<i; j++)
        cout<<"  ";
        for(int j=0; j<n-i; j++){
        cout<<a++<<" ";
        if (a>'Z')
        a='A';
        }
        cout<<endl;
    }
    // Please write your code here.
    return 0;
}