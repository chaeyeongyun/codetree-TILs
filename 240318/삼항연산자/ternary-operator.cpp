#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    int score, grade;
    std::cin >> score;
    grade = (score == 100) ? 1:0;
    if (grade)
        std::cout << "pass";
    else
        std::cout << "failure";
    return 0;
}