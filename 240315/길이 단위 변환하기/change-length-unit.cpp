#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    double ft = 30.48;
    int mile = 160934;
    cout << fixed;
    cout.precision(1);
    cout << "9.2ft = " << ft * 9.2 << "cm" << endl;
    cout << "1.3mi = " << mile * 1.3 << "cm" << endl;
    return 0;
}