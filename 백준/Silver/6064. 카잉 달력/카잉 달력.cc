#include <iostream>
using namespace std;

int gcdFind(int a, int b) {  // a와 b의 최대공약수 구하는 함수
  if (a >= b) {
    a = a % b;
    if (a == 0) {
      return b;
    } else {
      return gcdFind(a, b);
    }
  } else if (a < b) {
    b = b % a;
    if (b == 0) {
      return a;
    } else {
      return gcdFind(a, b);
    }
  }
  return 0;
}

int main() {
  int T, M, N, x, y;
  cin >> T;
  for (int i = 0; i < T; i++) {
    cin >> M >> N >> x >> y;

    int gcd = gcdFind(M, N);
    int r1 = N / gcd;  // M * r1 = (M과 N의 최소공배수)
    int r2 = M / gcd;  // N * r2 = (M과 N의 최소공배수)

    int yearX = x;  // yearX: x에 계속 M이 더해질 수
    bool kaing = false;

    for (int i = 0; i < r1; i++) {
      if (i != 0) yearX += M;  // 최초 시행 제외하고 매번 M을 더해줌
      if ((yearX - y) % N ==
          0) {  // 이 식을 yearX % N == y로 세우면 틀림: N과 y값이 같은 경우
        cout << yearX << endl;
        kaing = true;
        break;
      }
    }
    if (!kaing) {
      cout << -1 << endl;
    }
  }
}