// 다익스트라

const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input = [];

readline.on("line", (line) => {
  if (line.trim() === "") {
    readline.close();
  } else {
    input.push(line);
  }
});

readline.on("close", () => {
  const N = parseInt(input[0].split(" ")[0]);
  const M = parseInt(input[0].split(" ")[1]);

  // 친구관계 정보 저장할 2차원 배열
  const friendship = [];
  for (let i = 0; i <= N; i++) {
    const row = [];
    for (let i = 0; i <= N; i++) {
      row.push(0);
    }
    friendship.push(row);
  }
  // a와 b가 친구면 b와 a가 친구
  for (let i = 1; i <= M; i++) {
    const A = parseInt(input[i].split(" ")[0]);
    const B = parseInt(input[i].split(" ")[1]);
    if (friendship[A][B] == 0) {
      friendship[A][B] = 1;
      friendship[B][A] = 1;
    }
  }

  let res;
  let min_bacon = 10001;

  // 1번부터 N번 사람까지 순차적으로 케빈 베이컨 수 구하기
  for (let a = 1; a <= N; a++) {
    // a의 케빈 베이컨 수 구하기
    // a번째 사람의 배열 초기화
    const this_friendship = [];
    const value = [];
    for (let i = 0; i <= N; i++) {
      value.push(101);
    }
    this_friendship.push(value);
    this_friendship[0][a] = 0;
    const status = [];
    for (let i = 0; i <= N; i++) {
      status.push(false);
    }
    this_friendship.push(status);

    // mid 바뀔 때마다 탐색
    let mid = a;
    for (let n = 1; n <= N; n++) {
      for (let b = 1; b <= N; b++) {
        // mid와 연결된 사람 반영
        if (
          mid != b &&
          friendship[mid][b] == 1 &&
          this_friendship[0][b] > this_friendship[0][mid] + 1
        )
          this_friendship[0][b] = this_friendship[0][mid] + 1;
      }

      this_friendship[1][mid] = true;
      // false인 사람 중 다음 mid 정하기
      let tmp = 101;
      for (let i = 1; i <= N; i++) {
        if (!this_friendship[1][i] && tmp > this_friendship[0][i]) {
          mid = i;
          tmp = this_friendship[0][i];
        }
      }
    }

    // console.log(this_friendship);

    // 결과 비교
    let this_bacon = 0;
    for (let i = 1; i <= N; i++) {
      this_bacon += this_friendship[0][i];
    }
    if (min_bacon > this_bacon) {
      min_bacon = this_bacon;
      res = a;
    }
  }

  console.log(res);
  process.exit();
});
