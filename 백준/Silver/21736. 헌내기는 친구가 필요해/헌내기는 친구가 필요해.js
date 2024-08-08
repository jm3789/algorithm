// DFS: 스택
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

  let my_i, my_j;
  let count = 0;

  // 2차원 배열에 캠퍼스 정보 저장
  const map = [];
  for (let i = 1; i < N + 1; i++) {
    map.push(input[i].split(""));
  }

  // I의 위치 찾기
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (map[i][j] == "I") {
        my_i = i;
        my_j = j;
        break;
      }
    }
  }

  // 스택 준비
  let stack = [[my_i, my_j]];

  // 4방향으로 탐색: 이걸 반복할 거다
  function check(a, b) {
    // 이미 방문한 곳이거나 막혀있으면 종료
    if (map[a][b] == "X") return;

    // 그렇지 않으면
    // 현재 위치가 P이면 count 증가
    if (map[a][b] == "P") count++;
    // 방문처리
    map[a][b] = "X";
    // stack에 넣기
    stack.push([a, b]);
  }

  // stack에 아무것도 안 남을 때까지 반복
  while (stack.length != 0) {
    /*
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < M; j++) {
        console.log(map[i]);
      }
    }
    console.log(stack);
    */

    let now = stack.pop();
    let now_i = now[0];
    let now_j = now[1];

    // 4방향 탐색
    if (now_i - 1 >= 0) check(now_i - 1, now_j);
    if (now_j - 1 >= 0) check(now_i, now_j - 1);
    if (now_i + 1 < N) check(now_i + 1, now_j);
    if (now_j + 1 < M) check(now_i, now_j + 1);
  }

  // 출력
  if (count == 0) {
    console.log("TT");
  } else {
    console.log(count);
  }

  process.exit();
});
