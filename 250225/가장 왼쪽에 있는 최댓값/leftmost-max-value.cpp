#include <iostream>

using namespace std;

int main() {
    int n;
    cin>>n;

    int num[1000];
    for(int i=0; i<n; i++)
    cin>>num[i];

    int index=n;
    int max_val=0;

    while(index!=0){
        int tmp_index=index;
        max_val=0;
    for(int i=0; i<index; i++){
        if(num[i]>max_val){
            max_val=num[i];
            tmp_index=i;
        }
    }
    cout<<tmp_index+1<<" ";
    index=tmp_index;
    }
    // Write your code here!

    return 0;
}
