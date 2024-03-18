#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    int height, weight;
    std::cin >> height, weight;
    int bmi;
    bmi = weight / (height * height);
    std::cout << bmi;
    if (bmi > 25) {
        std::cout << "Obesty";
    }
    return 0;
}