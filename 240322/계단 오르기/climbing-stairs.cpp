#include <iostream>
#define MAXN 1000
using namespace std;

int dp[MAXN + 1] = {0, 0, 1, 1, 0, };

void print_dp(int n) {
    for (int i = 0; i <= n;i++) {
        cout << dp[i] << " ";
    }
    cout << endl;
}

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    for (int i = 4; i <= n; i++) {
        dp[i] = dp[i - 2] + dp[i - 3];
    }
    //print_dp(n);
    cout << dp[n] % 10007;
    return 0;
}