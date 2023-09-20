#include <iostream>
#include <string>
using namespace std;

int main() {
  int N, M;
  cin >> N >> M;

  string str = "";
  char c;

  for (int i = 0; i < M; i++) {
    cin >> c;
    str += c;
  }

  // index out of range 막기 위해 ..로 채움
  for (int i = 0; i < N; i++) {
    str += "..";
  }

  int res = 0;
  bool ioi;  // true면 res를 증가시킴

  for (int i = 0; i < M; i++) {
    if (str[i] == 'I') {  // 'I'를 만나면
      ioi = true;
      // N번 반복
      for (int j = 1; j <= N; j++) {
        // 다음으로 오는 문자가 순서대로 'O', 'I'가 아니라면
        if (!(str[i + 2 * j - 1] == 'O' && str[i + 2 * j] == 'I')) {
          ioi = false;  // ioi를 false로 전환,
          break;        // 반복 멈춤
        }
      }
      if (ioi) res++;
    }
  }

  cout << res << endl;

  return 0;
}