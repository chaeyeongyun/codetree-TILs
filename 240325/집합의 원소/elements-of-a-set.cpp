#include <stdio.h>
#include <iostream>
#define M 100000
using namespace std;

int parents[M + 1];


int find(int x)
{
    if (parents[x] == x) return x;
    int last = parents[x];
    parents[x] = find(parents[x]);
    return parents[x];
}

void union_chk(int a, int b)
{
    if (find(a) == find(b))
        printf("1\n");
    else
        printf("0\n");
}

void union_(int a, int b)
{
    int a_p = find(a), b_p = find(b);
    if (a_p != b_p)
    {
        parents[a_p] = b_p;
    }
}

void run(int ord, int a, int b)
{
    switch(ord)
    {
        case 0:
            union_(a, b);
            break;
        case 1:
            union_chk(a, b);
            break;
    }
}

void init(int n)
{
    for (int i = 1; i <= n; i++)
        parents[i] = i;
}

int main() 
{
    int n, m;
    scanf("%d %d\n", &n, &m);
    init(n);
    int ord, a, b;
    for (int i = 0; i < m; i++)
    {
        scanf("%d %d %d\n", &ord, &a, &b);
        run(ord, a, b);
    }
    return 0;
}