#include <iostream>
using namespace std;

int main() {
    double sum=0;

    for(int i=0; i<8; i++){
        double score;
        cin>>score;

        sum+=score;
    }

    cout<<fixed;
    cout.precision(1);
    cout<<sum/8;
    // Please write your code here.
    return 0;
}