#include <iostream>
#define MAXN 1000
using namespace std;

int dp[MAXN + 1] = {0, 0, 1, 1, 0, };
int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    for (int i = 4; i <= n; i++) {
        for (int j = 2; j <= i / 2; j++) {
            dp[i] += dp[j] * dp[i - j];
        }
    }
    cout << dp[n];
    return 0;
}