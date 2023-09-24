#include <iostream>
#include <vector>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);

  int N, M;
  cin >> N >> M;
  long num;

  vector<int> sums(N + 1);
  sums[0] = 0;

  for (int i = 1; i <= N; i++) {
    cin >> num;
    sums[i] = sums[i - 1] + num;
  }
  for (int i = 0; i < M; i++) {
    int s1, s2;
    cin >> s1 >> s2;
    cout << sums[s2] - sums[s1 - 1] << '\n';
  }

  return 0;
}