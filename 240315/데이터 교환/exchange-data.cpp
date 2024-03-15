#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a = 5, b = 6, c = 7;
    int temp1, temp2;
    temp1 = b;
    temp2 = c;
    b = a;
    c = temp1;
    a = temp2;
    cout << a << endl;
    cout << b << endl;
    cout << c;
    return 0;
}