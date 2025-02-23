#include <iostream>
using namespace std;

int main() {
    int max_val=0;
    for(int i=0; i<10; i++){
        int num;
        cin>>num;

        if(num>max_val)
        max_val=num;
    }

    cout<<max_val;
    // Please write your code here.
    return 0;
}