#include <iostream>
#include <map>
#include <string>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    string str;
    map<string, int> str_cnt;
    cin >> n;
    for (int i; i < n; i++) {
        // 각 문자열의 개수 map에 저장
        cin >> str;
        // 해당 문자열이 처음 들어온 경우 1로 초기화
        if (str_cnt.find(str) == str_cnt.end()) {
            str_cnt[str] = 1;
            continue;
        }
        str_cnt[str] += 1;
    }
    map<string, int>::iterator it;
    for (it=str_cnt.begin();it!=str_cnt.end();it++) {
        cout << fixed;
        cout.precision(4);
        cout << it -> first << " " << 100 * (it -> second) / double(n) << endl;
    }
    return 0;
}