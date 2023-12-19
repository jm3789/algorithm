#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<pair<int, int>> l;

  for (int i = 0; i < n; i++) {
    int startTime, endTime;
    cin >> startTime >> endTime;  // 종료시간인 b로 sort해야 함
    l.push_back(make_pair(endTime, startTime));  // (종료시간, 시작시간)
  }
  sort(l.begin(), l.end());

  vector<pair<int, int>> ans;
  ans.push_back(l[0]);  // 일단 맨 첫번째에 있는 회의를 넣는다
  int startTime = l[0].second;  // 마지막으로 결정된 회의의 시작시간
  int endTime = l[0].first;  // 마지막으로 결정된 회의의 종료시간

  for (int j = 1; j < l.size(); j++) {
    // 같은 시간에 끝나는 회의가 이미 존재함
    if (endTime == l[j].first) {
      // 시작하자마자 끝나는 회의가 아니라면 넣지 말기
      if (l[j].first == l[j].second) {
        ans.push_back(l[j]);
      }
      continue;
    }
    // 더 늦은 시간에 끝나는 회의인 경우 endTime보다 시작시간이 같거나 늦어야
    // 됨
    if (endTime <= l[j].second) {
      ans.push_back(l[j]);
      startTime = l[j].second;
      endTime = l[j].first;
    }
  }

  cout << ans.size() << endl;
}