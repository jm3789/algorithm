#include <iostream>
#include <queue>
#include <tuple>

using namespace std;

int main() {
  int M, N;
  cin >> M >> N;

  int tomatoFarm[N][M];

  // tomatoFarm 입력받고 세팅
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      cin >> tomatoFarm[i][j];
    }
  }

  // 큐 세팅
  queue<tuple<int, int>> q;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      if (tomatoFarm[i][j] == 1) {
        q.push(make_tuple(i, j));
      }
    }
  }

  int vList[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
  int day = -1;

  while (!q.empty()) {
    day++;
    int repeat = q.size();
    for (int k = 0; k < repeat; k++) {
      // 익은 토마토의 위치 (A, B)
      int A = get<0>(q.front());
      int B = get<1>(q.front());

      // 인접한 토마토의 위치 (a, b)
      for (int i = 0; i < 4; i++) {
        int a = A + vList[i][0];
        int b = B + vList[i][1];
        if (0 <= a && a < N && 0 <= b &&
            b < M) {  // (a, b)가 농장 범위 안에 있을 때
          if (tomatoFarm[a][b] ==
              0) {  // (a, b) 위치의 토마토가 안 익었으면 1로 바꾸고 push
            tomatoFarm[a][b] = 1;
            q.push(make_tuple(a, b));
          }
        }
      }
      q.pop();
    }
  }

  // 다 익었는지 확인: 다 안익었다면 day를 -1로
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      if (tomatoFarm[i][j] == 0) {
        day = -1;
        break;
      }
    }
  }

  // 출력
  cout << day << endl;

  return 0;
}
