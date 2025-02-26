#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Jewel {
    int weight;
    int value;
    double per;
    
    bool operator<(struct Jewel right) {
        if (per > right.per) return true;
        if (per < right.per) return false;
        return false;
    }
};

int main() {
    int n, m;
    cin >> n >> m;

    vector<struct Jewel> jewels(n);
    for (int i = 0; i < n; i++) {
        int w, v;
        cin >> w >> v;
        
        jewels[i].weight = w;
        jewels[i].value = v;
        jewels[i].per = double(v) / w;
    }

    sort(jewels.begin(), jewels.end());

    double ans = 0;
    double total_weight = 0;
    for (int i = 0; i < n; i++) {
        if (jewels[i].weight <= m - total_weight) {
            total_weight += jewels[i].weight;
            ans += jewels[i].value;
        }
        else {
            ans += jewels[i].value * ((m - total_weight) / jewels[i].weight);
            break;
        }

        if (total_weight >= m)
            break;
    }

    cout << fixed;
    cout.precision(3);

    cout << ans;
    // Please write your code here.
    return 0;
}