#include <iostream>
#include <climits>

using namespace std;

int main() {
    int n;
    cin>>n;

    int max_val=INT_MIN;
    int second_val=max_val+1;

    for(int i=0; i<n;i++){
        int num;
        cin>>num;

        if(num>max_val){
            second_val=max_val;
            max_val=num;
        }
        else if (num<max_val && num>second_val)
        second_val=num;
    }

    cout<<max_val<<" "<<second_val;
    // Write your code here!

    return 0;
}
