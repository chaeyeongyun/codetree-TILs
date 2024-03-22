#include <iostream>
#define MAXN 45

using namespace std;

int fibo[MAXN + 1] = {0, 1, 1, 0, };

int main() {
    int N;
    cin >> N;
    for (int i = 3; i <= N; i++) {
        fibo[i] = fibo[i - 1] + fibo[i - 2];
    }
    cout << fibo[N];
    return 0;
}