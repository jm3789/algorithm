#include <iostream>
#include <string>
#include <vector>

using namespace std;

void clearFlagVector();
void areaCntPrint();
void areaSearch(int X, int Y);

int N;
vector<string> stringVector;     // 각 칸의 색깔 정보
vector<vector<int>> flagVector;  // 각 칸의 탐색 여부
int dir[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

int main() {
  string str;
  cin >> N;
  flagVector = vector<vector<int>>(N, vector<int>(N, 0));

  for (int i = 0; i < N; i++) {
    cin >> str;
    stringVector.push_back(str);
  }

  // 첫번째 결과
  areaCntPrint();

  // 적록색약 시점으로 바꿔주기: 초록색을 빨간색으로
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (stringVector[i][j] == 'G') {
        stringVector[i][j] = 'R';
      }
    }
  }

  // 두번째 결과
  areaCntPrint();

  return 0;
}

// 각 칸의 탐색 여부를 모두 초기화하는 함수
void clearFlagVector() {
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      flagVector[i][j] = 0;
    }
  }
}

// 구역의 개수를 구해 출력하는 함수
void areaCntPrint() {
  clearFlagVector();
  int cnt = 0;

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (flagVector[i][j] == 0) {
        cnt++;
        areaSearch(i, j);
      }
    }
  }
  cout << cnt << ' ';
}

// 재귀적으로 실행되는 함수. dfs탐색을 수행함
void areaSearch(int X, int Y) {
  if (flagVector[X][Y] == 0) {
    flagVector[X][Y] = 1;
    for (int v = 0; v < 4; v++) {
      int x = X + dir[v][0];
      int y = Y + dir[v][1];
      if (0 <= x && x <= N - 1 && 0 <= y && y <= N - 1) {
        if (stringVector[X][Y] == stringVector[x][y]) {
          areaSearch(x, y);
        }
      }
    }
  }
}
