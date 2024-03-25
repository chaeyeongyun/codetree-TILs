#include <iostream>
#include <stdio.h>
#include <vector>
#define M 10000
using namespace std;

int n;
int depth[M + 1];
vector<int> children[M + 1];
int parent[M + 1];

// --- dfs를 통해 자식의 깊이를 부모의 깊이 + 1로 갱신---
void dfs(int x)
{
    for (int i = 0; i < (int) children[x].size(); i++)
    {
        int y = children[x][i];
        depth[y] = depth[x] + 1;
        dfs(y);
    }
}

int main()
{
    scanf("%d", &n);
    int a, b;
    for (int i = 0; i < (n - 1); i++)
    {
        scanf("%d %d", &a, &b);
        children[a].push_back(b);
        parent[b] = a;
    }
    scanf("%d %d", &a, &b);
    // root node 찾기
    int root_node = 0;
    for (int i = 1; i <= n; i++)
    {
        if (parent[i] == 0)
            root_node = i;
    }
    // 전처리 : dfs를 통해 자식의 깊이를 부모의 깊이 + 1로 갱신한다.
    depth[root_node] = 1;
    dfs(root_node);
    // ---step 1---
    // 두 노드 a와 b의 depth를 비교해 더 큰 쪽의 노드를 골라 부모를 따라가며 더 작은 쪽 depth로 맞춰준다
    while (depth[a] != depth[b]) 
    {
        if (depth[a] > depth[b])
            a = parent[a];
        else
            b = parent[b];
    }
    // ---step2---
    // 두 노드 a, b가 일치해질 때까지 한 칸씩 위로
    while (a != b)
    {
        a = parent[a];
        b = parent[b];
    }
    printf("%d", a);
    return 0;
}