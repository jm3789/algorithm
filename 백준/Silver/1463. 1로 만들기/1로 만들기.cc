// 그리디 알고리즘으로 풀 수 없음
// DP로 해결

#include <iostream>

using namespace std;

int main() {
  int N;
  cin >> N;

  int dp[N + 1]; // N+1의 크기를 가진 정수 배열 생성
  int cnt = 0;

  // 초기값 설정
  dp[1] = 0;
  dp[2] = 1;
  dp[3] = 1;

  // dp[i]는 dp[n/3], dp[n/2], dp[n-1] 에 들어있는 값들 중 가장 작은 값에 1을
  // 더한 값이 됨
  for (int i = 4; i < N + 1; i++) {
    if (i % 3 == 0 && i % 2 == 0) {
      dp[i] = min(min(dp[i / 3], dp[i / 2]), dp[i - 1]) + 1;
    } else if (i % 3 == 0) {
      dp[i] = min(dp[i / 3], dp[i - 1]) + 1;
    } else if (i % 2 == 0) {
      dp[i] = min(dp[i / 2], dp[i - 1]) + 1;
    } else {
      dp[i] = dp[i - 1] + 1;
    }
  }

  cout << dp[N] << endl;
}
