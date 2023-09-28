#include <iostream>
using namespace std;

int main() {
  long long X, Y, W, S;

  cin >> X >> Y >> W >> S;

  unsigned long long res;

  if (W * 2 <= S) {  // a) 한 블록씩 이동
    res = (X + Y) * W;
  } else if (W > S) {  // b) 대각선으로만 이동
    res = max(X, Y) * S;
    if ((X + Y) % 2 == 1) {  // 대각선의 개수가 맞아떨어지지 않는 경우
      res = res - S + W;
    }
  } else {  // c) 대각선으로 이동 + 한 블록씩 이동
    res = min(X, Y) * S + abs(X - Y) * W;
  }

  cout << res << endl;
}