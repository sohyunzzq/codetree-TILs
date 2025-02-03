#include <iostream>
using namespace std;

int main() {
    char a;
    cin>>a;

    if (a=='S')
    cout<<"Superior";
    else if(a=='A')
    cout<<"Excellent";
    else if (a=='B')
    cout<<"Good";
    else if (a=='C')
    cout<<"Usually";
    else if (a=='D')
    cout<<"Effort";
    else
    cout<<"Failure";
    // Please write your code here.
    return 0;
}