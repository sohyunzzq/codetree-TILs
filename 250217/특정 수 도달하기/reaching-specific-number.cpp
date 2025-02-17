#include <iostream>
using namespace std;

int main() {
    int sum=0;
    int index=10;
    for(int i=0; i<10; i++){
        int n;
        cin>>n;

        if(n>=250){
            index =i;
        break;
        }

        sum+=n;
    }
    cout<<fixed;
    cout.precision(1);
    cout<<sum<<" "<<(double)sum/index;
    // Please write your code here.
    return 0;
}