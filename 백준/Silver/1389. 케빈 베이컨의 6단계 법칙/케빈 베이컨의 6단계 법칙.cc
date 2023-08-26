// BFS. 큐 이용

// + 플로이드 워셜 알고리즘이 더 효율적이다. 공부해보기

#include <iostream>
#include <queue>
#include <tuple>
#include <vector>

using namespace std;

int main() {
  int N, M;
  cin >> N >> M;

  // 벡터 배열 friendship 만들기
  // 첫번째 인덱스는 유저의 번호(1~N)
  // 해당 유저의 친구(최대 N-1명) 번호 벡터가 들어있음

  vector<int> friendship[N + 1];
  for (int i = 0; i < M; i++) {  // 친구 정보 등록하기
    int A, B;
    cin >> A >> B;
    // A의 친구로 B를 등록
    friendship[A].push_back(B);
    // B의 친구로 A를 등록
    friendship[B].push_back(A);
  }

  // 계산
  int res;  // 현재 케빈 베이컨 수가 가장 작은 사람
  int minKbNum = 99 * 99;  // 현재 가장 작은 케빈 베이컨 수

  // a번 유저의 케빈 베이컨 수 구하기
  for (int a = 1; a <= N; a++) {  // a번 유저는 1번 유저 ~ N번 유저
    // cout << "a:" << a << endl;
    int kbNum = 0;  // kbNum: a번 유저의 케빈 베이컨 수

    for (int b = 1; b <= N; b++) {
      // cout << "b:" << b << endl;
      if (a == b) {
        continue;
      }
      // a번 유저와 b번 유저 사이의 케빈 베이컨 수가 얼마인지 추적
      queue<tuple<int, int>> q;
      int cnt = 0;
      q.push(make_tuple(a, cnt));

      while (get<0>(q.front()) != b) {
        cnt = get<1>(q.front());
        int idx = get<0>(q.front());
        for (int elem : friendship[idx]) {
          q.push(make_tuple(elem, cnt + 1));
        }
        q.pop();
      }
      // cout << get<1>(q.front()) << endl;

      // 결과를 kbNum에 더해준다
      kbNum += get<1>(q.front());
    }

    // cout << "kbNum for " << a << ": " << kbNum << endl;
    // a의 kbNum이 minKbNum보다 작으면 a를 res에 기억
    if (kbNum < minKbNum) {
      minKbNum = kbNum;
      res = a;
    }
  }

  cout << res << endl;

  return 0;
}