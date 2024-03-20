#include <iostream>
#include <map>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    map<int, int> m;
    cin >> n;
    int num;
    for (int i = 0;i < n; i++) {
        cin >> num;
        m.insert({num, i + 1});
    }
    map<int, int>::iterator it;
    for (it=m.begin();it!=m.end();it++) {
        cout << it -> first << " " << it -> second << endl;
    }
    return 0;
}