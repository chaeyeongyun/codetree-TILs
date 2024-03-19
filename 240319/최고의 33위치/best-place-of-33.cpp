#include <iostream>
#include <stdio.h>

int max(int a, int b) {
    if (a > b)
        return a;
    else
        return b;
}

int main() {
    int N;
    scanf("%d", &N);
    int arr[N][N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            std::cin >> arr[i][j];
        }
    }
    int max_coin = 0;
    int temp;
    for (int i = 0; i < N - 2; i++) {
        for (int j = 0; j < N - 2; j++) {
            temp = 0;
            for (int k = 0; k < 3; k++){
                for (int l = 0; l < 3; l++) {
                    temp += arr[i + k][j + l];
                }
            }
            max_coin = max(max_coin, temp);
        }    
    }
    printf("%d", max_coin);
    return 0;
}