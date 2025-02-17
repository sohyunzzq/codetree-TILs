#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;

    double sum=0;
    for(int i=0; i<n; i++){
        double tmp;
        cin>>tmp;

        sum+=tmp;
    }

    cout<<fixed;
    cout.precision(1);

    double grade=sum/n;
    cout<<grade<<endl;

    if (grade>=4 )
    cout<<"Perfect";
    else if (grade>=3)
    cout<<"Good";
    else
    cout<<"Poor";
    // Please write your code here.
    return 0;
}