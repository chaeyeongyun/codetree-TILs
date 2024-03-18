#include <iostream>

int min(int a, int b) {
    if (a < b)
        return a;
    else
        return b;
}

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b, c;
    cin >> a >> b >> c;
    cout << min(min(a, b), c);
    return 0;
}