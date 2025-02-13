#include <iostream>

using namespace std;

int start, e;

int main() {
    cin >> start >> e;

    int cnt=0;

    for(int i=start; i<=e; i++){
        int tmp=0;
        for(int j=1; j<=i; j++){
            if (i%j==0)
            tmp++;
        }
        if(tmp==3)
        cnt++;
    }

    cout<<cnt;

    // Write your code hre!

    return 0;
}
