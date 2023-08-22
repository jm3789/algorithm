// 이분 탐색

#include <iostream>

using namespace std;

int findHeight(int* trees, int start, int end, int M, int N, int result) {
  if (start > end) {
    return result;
  } else {
    int mid = (start + end) / 2;
    long long wood = 0;  // 2,147,483,647을 넘어가는 값
    for (int i = 0; i < N; i++) {
      wood +=
          max(0, trees[i] - mid);  // mid보다 큰 나무들을 잘랐을 때만 더해주기
    }
    if (wood < M) {  // 나무의 길이가 부족함: 절단기의 높이를 낮게 설정하기
      return findHeight(trees, start, mid - 1, M, N, result);
    } else {  // 나무의 길이가 충분함: mid를 result로 저장하고 절단기의 높이를
              // 높게 설정하기
      return findHeight(trees, mid + 1, end, M, N, mid);
    }
  }
}

int main() {
  int N, M;
  cin >> N >> M;

  int trees[N];
  int tree;
  int maxTree = 0;  // 가장 높은 나무의 길이

  for (int i = 0; i < N; i++) {
    cin >> tree;
    trees[i] = tree;
    if (tree > maxTree) {
      maxTree = tree;
    }
  }
  cout << findHeight(trees, 0, maxTree, M, N, 0) << endl;
}