#include <iostream>
using namespace std;

#define SZ 1001
#define MOD 10007

int DP[SZ];

int main() {
    int n;
    cin>>n;

    DP[0]=0;
    DP[1]=1;
    DP[2]=2;
    
    for(int i=3; i<=n; i++) {
        DP[i]=(DP[i-1]+DP[i-2])%MOD;
    }

    cout<<DP[n];
}