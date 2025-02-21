#include <iostream>
using namespace std;

int main() {
    int n1, n2;
    cin>>n1>>n2;

    int arr1[100], arr2[100];
    for(int i=0; i<n1; i++)
    cin>>arr1[i];
    for(int i=0; i<n2; i++)
    cin>>arr2[i];

    int flag=1;

    if (n1>=n2){
        for(int i=0; i<=n1-n2; i++) {
            if (arr1[i]==arr2[0]) {
                for(int j=0; j<n2; j++) {
                    if (arr1[i+j] != arr2[j]){
                    flag=0;
                    break;
                    }
                }
            }
        }
    }
    else
    flag=0;

    cout<<(flag?"Yes":"No");

    // Please write your code here.
    return 0;
}