#include <iostream>
using namespace std;

int main() {
    double sum=0;
    int index=10;

    for(int i=0; i<10; i++){
        int n;
        cin>>n;

        if(n==0){
            index = i;
            break;
        }

        sum+=n;
    }

    cout<<fixed;
    cout.precision(1);

    cout<<(int)sum <<" "<<sum/index;
    // Please write your code here.
    return 0;
}