const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

readline.on("line", (line) => {
  if (line.trim() === "") {
    readline.close();
  } else {
    input.push(line.split(" "));
  }
});

readline.on("close", () => {
  // Map 객체: key-value 쌍을 저장함
  // 검색할 때 시간 복잡도가 O(1)
  const N = parseInt(input[0][0]);
  const M = parseInt(input[0][1]);
  const myMap = new Map();
  let i;
  for (i = 1; i <= N; i++) {
    myMap.set(input[i][0], input[i][1]);
  }
  while (i <= N + M) {
    console.log(myMap.get(input[i][0]));
    i++;
  }
});
