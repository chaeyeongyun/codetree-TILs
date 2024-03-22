#include <iostream>
#define MAXN 1000
using namespace std;

int dp[MAXN + 1] = {0, 1, 2, 0, };

int main() {
    int n;
    cin >> n;
    for (int i = 3; i <= n; i++) {
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;
    }
    cout << dp[n];
    return 0;
}