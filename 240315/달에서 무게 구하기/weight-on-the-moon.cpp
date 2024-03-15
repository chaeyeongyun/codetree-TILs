#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    double gravity = 0.165;
    int weight = 13;
    cout << fixed;
    cout.precision(6);
    cout << weight << " * " << gravity << " = " << weight * gravity;
    return 0;
}