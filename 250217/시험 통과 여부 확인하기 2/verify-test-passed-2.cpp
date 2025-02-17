#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;
    
    int cnt=0;
    for(int i=0; i<n; i++){
        int sum=0;

        for(int j=0; j<4; j++){
            int score;
        cin>>score;
        sum+=score;
        }

        if (double(sum)/4>=60){
        cout<<"pass";
        cnt++;
        }
        else
        cout<<"fail";
        cout<<endl;
    }
    cout<<cnt;
    // Please write your code here.
    return 0;
}