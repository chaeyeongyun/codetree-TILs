#include <iostream>
#include <map>
#include <string>
using namespace std;

map<int, int> m;

void add(int k, int v){
    // m.insert({k, v});  덮어쓰기 안됨
    m[k] = v;
}

void remove(int k){
    m.erase(k);
}

void find(int k){
    if (m.find(k) != m.end())
        cout << m[k]<< endl;
    else
        cout << "None" << endl;
}

void print_list() {
    if (m.empty()) {
        cout << "None" << endl;
        return;
    }
    
    map<int, int>::iterator it;
    for (it = m.begin(); it != m.end(); it++) {
        cout << it -> second << " ";
    }
    cout << endl;
}

int main() {
    int n;
    cin >> n;
    string ord;
    int a, b;
    for (int i = 0; i < n; i++) {
        cin >> ord;
        if (ord == string("add")){
            cin >> a >> b;
            add(a, b);
        }
        else if (ord == string("find")) {
            cin >> a;
            find(a);
        }
        else if (ord == string("remove")) {
            cin >> a;
            remove(a);
        }
        else if (ord == string("print_list")) {
            print_list();
        }
    }
    return 0;
}