#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;
    cin >> a >> b;
    if (a < b) {
        cout << b - a;
    }
    else {
        cout << a - b;
    }
    return 0;
}