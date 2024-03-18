#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    float height, weight;
    int bmi;
    std::cin >> height >> weight;
    height /= 100;
    bmi = weight / (height * height);
    std::cout << bmi << std::endl;
    if (bmi >= 25) {
        std::cout << "Obesity";
    }
    return 0;
}