#include <iostream>
using namespace std;

int main() {
    int sum=0;
    int cnt=0;

    for(int i=0; i<10; i++){
        int n;
        cin>>n;

        if(n==0)
        break;

        if(n % 2==0){
        sum+=n;
        cnt++;
        }
    }
    cout<<cnt<<" "<<sum;
    // Please write your code here.
    return 0;
}