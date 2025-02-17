#include <iostream>
using namespace std;

int main() {
    int arr[10];
    for(int i=0; i<10; i++)
    cin>>arr[i];

    int sum=0;
    for(int i=1; i<10; i+=2)
    sum+=arr[i];
    
    cout<<sum<<" ";

    sum=0;
    for(int i=2; i<10; i+=3)
    sum+=arr[i];

    cout<<fixed;
    cout.precision(1);
    cout<<double(sum)/3;
    // Please write your code here.
    return 0;
}