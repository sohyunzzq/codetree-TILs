#include <iostream>
using namespace std;

int main() {
    int h, w;
    cin>>h>>w;

    double b = (10000*w)/(h*h);

    cout<<b<<endl;
    if (b>=25)
    cout<<"Obesity";
    // Please write your code here.
    return 0;
}