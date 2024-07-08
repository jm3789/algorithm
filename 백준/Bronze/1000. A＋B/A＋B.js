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
  let arr = input[0].split(" ").map((n) => parseInt(n));
  console.log(arr[0] + arr[1]);
  process.exit();
});
