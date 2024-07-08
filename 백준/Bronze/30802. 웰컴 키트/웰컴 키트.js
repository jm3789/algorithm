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
  // 첫째 줄: 각 사이즈의 필요한 장수를 T로 나눈 결과를 올림하여 모두 더함
  // 둘째 줄: N을 P로 나누었을 때 몫과 나머지

  const N = parseInt(input[0]);
  const T = parseInt(input[2].split(" ")[0]);
  const P = parseInt(input[2].split(" ")[1]);

  let res1 = 0;
  input[1].split(" ").map((n) => {
    n = Math.ceil(parseInt(n) / T);
    res1 += n;
  });

  const res2 = `${Math.floor(N / P)} ${N % P}`;

  console.log(res1);
  console.log(res2);
  process.exit();
});
