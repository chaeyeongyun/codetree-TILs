#include <iostream>
#define MAXN 1000;
using namespace std;

int dp[] = {0, 2, 7, 0, };

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        dp[i] = ((dp[i - 1] * dp[1]) + (dp[i - 2] * dp[2])) % 1000000007;
    }
    cout << dp[n];
    return 0;
}