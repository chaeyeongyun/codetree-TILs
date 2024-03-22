#include <iostream>
#define MAXN 1000
using namespace std;

long long dp[MAXN + 1] = {1, 2, 7, 0, };

int sum(int x){
    int ans = 0;
    for (int i = 0; i <= x; i++){
        ans += dp[i];
    }
    return ans;
}

int main() {
    int n;
    cin >> n;
    for (int i = 3; i <= n; i++) {
        dp[i] = ((dp[i - 1] * 2) + (dp[i - 2] * 3) + 2 * sum(i - 3)) % 1000000007;
    }
    cout << dp[n];
    return 0;
}