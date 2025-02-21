#include <iostream>
using namespace std;

int main() {
    int n, q;
    cin>>n>>q;

    int num[100];

    for(int i=0; i<n; i++)
    cin>>num[i];

    for(int i=0; i<q; i++){
        int cmd;
        cin >>cmd;

        if(cmd == 1){
            int index;
            cin>>index;

            cout<<num[index-1];
        }
        else if (cmd ==2){
            int val;
            cin>>val;

            int ans =0;

            for(int j=0; j<n; j++)
            if(val == num[j]){
            ans=j+1;
            break;
            }

            cout<<ans;
        }
        else {
            int start, end;
            cin>>start>>end;

            for(int j=start-1; j<end; j++)
            cout<<num[j]<<" ";
        }
        cout<<endl;
    }

    // Please write your code here.
    return 0;
}