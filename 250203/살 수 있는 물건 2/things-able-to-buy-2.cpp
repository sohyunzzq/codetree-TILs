#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;

    if (n>=3000)
    cout<<"book";
    else if(n>=1000)
    cout<<"mask";
    else if(n>=500)
    cout<<"pen";
    else
    cout<<"no";
    // Please write your code here.
    return 0;
}