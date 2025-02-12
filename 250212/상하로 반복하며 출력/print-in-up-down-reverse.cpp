#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;
    int up=1;
    int down=n;

    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            if(j%2==0) {
                cout << up;
            }
            else
            cout<<down;
        }
        up++;
        down--;
        cout<<endl;
    }
    // Please write your code here.
    return 0;
}