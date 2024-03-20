#include <iostream>
#include <string>
#include <map>

using namespace std;

// 변수 선언
int n;
map<int, int> m;

int main() {
    // 입력:
    cin >> n;
    for(int i = 0; i < n; i++) {
        string command;
        cin >> command;

        if(command == "add") {
            int k, v;
            cin >> k >> v;
            m[k] = v;
        }
        else if(command == "remove") {
            int k;
            cin >> k;
            m.erase(k);
        }
        else if(command == "find") {
            int k;
            cin >> k;
            if(m.find(k) == m.end())
                cout << "None" << endl;
            else
                cout << m[k] << endl;
        }
        else {
            if(m.empty()) {
                cout << "None" << endl;
                continue;
            }
            map<int, int>::iterator it;
            for(it = m.begin(); it != m.end(); it++)
                cout << it -> second << " ";
            cout << endl;
        }
    }
    return 0;
}