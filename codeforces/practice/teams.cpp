#include <iostream>

using namespace std;

int main() {
    int n, k, count=0, part;
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> part;
        if (5-part>=k) {
            count++;
        }
    }
    cout << count/3 << endl;
    return 0;
}