#include <iostream>
using namespace std;

int main() {
    int a=5, b=6, c=7;
    int tmp = b;
    b=a;
    int tmp2 = c;
    c = tmp;

    a = tmp2;

    cout<<a<<endl<<b<<endl<<c;
    // Please write your code here.
    return 0;
}