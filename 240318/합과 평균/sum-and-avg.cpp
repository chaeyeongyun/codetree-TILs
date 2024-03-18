#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;
    cin >> a >> b;
    cout << fixed;
    cout.precision(1);
    cout << a + b << " " << (a + b) / 2.0;
    return 0;
}