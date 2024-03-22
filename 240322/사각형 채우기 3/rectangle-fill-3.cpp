#include <iostream>
#define MAXN 1000
using namespace std;

int dp[MAXN + 1] = {1, 2, 7, 0, };

int sum(int x){
    int ans = 0;
    for (int i = 0; i <= x; i++){
        ans += dp[i] % 1000000007;
    }
    return ans;
}

int main() {
    int n;
    cin >> n;
    for (int i = 3; i <= n; i++) {
        dp[i] = ((dp[i - 1] * 2) + (dp[i - 2] * 3) ) % 1000000007;
        for (int j = (i - 3); j >= 0; j--) {
            dp[i] += 2 * sum(i - 3) % 1000000007;
        }
    }
    cout << dp[n];
    return 0;
}