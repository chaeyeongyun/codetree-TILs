#include <iostream>
#define MAXN 1000
using namespace std;

int dp[MAXN + 1] = {1, 2, 7, 0, };

int main() {
    int n;
    cin >> n;
    for (int i = 3; i <= n; i++) {
        dp[i] = ((dp[i - 1] * 2) + (dp[i - 2] * 3)) % 1000000007;
        for (int j = (i - 3); j >= 0; j--) {
            dp[i] = (dp[i] + (2 * dp[j])) % 1000000007;
        }
    }
    cout << dp[n];
    return 0;
}