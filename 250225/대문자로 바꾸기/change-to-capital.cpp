#include <iostream>
using namespace std;

int main() {
    char alpha[5][3];
    for(int i=0; i<5; i++)
    for(int j=0; j<3; j++)
    cin>>alpha[i][j];

    for(int i=0; i<5; i++){
    for(int j=0; j<3; j++)
    cout<<char(alpha[i][j]-'a'+'A')<<" ";
    cout<<endl;
    }
    // Please write your code here.
    return 0;
}