#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
  int n, m, u, v;
  cin >> n >> m;
  vector<vector<int>> g;
  for (int i = 0; i <= n; i++) {
    vector<int> vertex;
    g.push_back(vertex);
  }

  int mark[n + 1] = {
      0,
  };

  for (int i = 0; i < m; i++) {
    cin >> u >> v;
    // 같은 간선은 한 번만 주어진다
    g[u].push_back(v);
    g[v].push_back(u);
  }

  int componentNumber = 0;
  queue<int> q;

  for (int i = 1; i <= n; i++) {
    if (mark[i] == 0) {
      componentNumber++;
      for (int j = 0; j < g[i].size(); j++) {
        q.push(g[i][j]);
      }
      mark[i] = 1;
      while (!q.empty()) {
        int v = q.front();
        q.pop();
        if (mark[v] == 0) {
          mark[v] = 1;
          for (int j = 0; j < g[v].size(); j++) {
            q.push(g[v][j]);
          }
        }
      }
    }
  }

  cout << componentNumber << endl;
  return 0;
}