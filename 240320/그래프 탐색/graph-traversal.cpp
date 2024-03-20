#include <iostream>
#include <vector>
#define MAX_NUM 1000

using namespace std;

int n, m; // n개의 정점 m개의 간선
int answer; // 1정점으로부터 갈 수 있는 노드 수

// 노드가 1부터 시작이므로 MAX_NUM + 1로 한다.
vector<int> graph[MAX_NUM + 1];
// 양방향이므로 visited설정하여 dfs수행
bool visited[MAX_NUM + 1] = {false,};

void dfs(int vertex) {
    // vertex에서 이어져있는 모든 정점 탐색
    for (int i = 0; i < (int) graph[vertex].size(); i++) {
        int curr_v = graph[vertex][i];
        if (!visited[curr_v]) { // 방문한 적 없으면
            visited[curr_v] = true;
            answer++;
            dfs(curr_v);
        }   
    }
}

int main() {
    cin >> n >> m;
    int v1, v2;
    for (int i = 0; i < m; i++) {
        // 각 정점이 서로 이동 가능한 양방향 그래프
        // 각 정점에 대한 간선 각각 저장
        cin >> v1 >> v2;
        graph[v1].push_back(v2);
        graph[v2].push_back(v1);
    }
    visited[1] = true;
    dfs(1);

    cout << answer;
    return 0;
}