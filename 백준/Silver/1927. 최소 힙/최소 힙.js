// 최소 힙: 부모 노드가 자식 노드보다 항상 작은 완전 이진 트리
// 힙의 루트 노드(0번 인덱스)가 항상 가장 작은 값을 가지도록 유지한다.
// insert: 새로운 요소를 힙에 추가하고 upheap 과정을 통해 올바른 위치로 이동
// pop: 루트 노드를 pop하고 마지막 노드를 루트로 이동한 뒤 downheap 과정을 통해 올바른 위치로 이동

class MinHeap {
  constructor() {
    this.heap = [];
  }
  swap(index1, index2) {
    // 구조 분해 할당 사용해 swap
    [this.heap[index1], this.heap[index2]] = [
      this.heap[index2],
      this.heap[index1],
    ];
  }

  insert(x) {
    this.heap.push(x);
    // TODO: 마지막 요소를 upheap으로 자리 지정
    let index = this.heap.length - 1;
    while (index > 0) {
      let upIndex = Math.ceil(index / 2) - 1;
      if (x < this.heap[upIndex]) this.swap(index, upIndex);
      else break;
      index = upIndex;
    }
  }

  pop() {
    if (this.heap.length == 0) return 0;
    // 첫 요소(root)와 마지막 요소의 자리를 바꿈
    this.swap(0, this.heap.length - 1);
    // 마지막 요소를 pop
    let r = this.heap.pop();
    // TODO: 첫 요소를 downheap으로 자리 지정
    let n = this.heap[0];
    let index = 0;
    // 왼쪽 자식 없을 때까지 진행
    while (index * 2 + 1 <= this.heap.length - 1) {
      let downIndex = index * 2 + 1;
      // 오른쪽 자식이 있다면 둘 중 더 작은 요소를 골라
      if (downIndex + 1 <= this.heap.length - 1) {
        if (this.heap[downIndex] > this.heap[downIndex + 1]) downIndex++;
      }
      // 부모보다 작다면 swap
      if (n > this.heap[downIndex]) this.swap(index, downIndex);
      else break;
      index = downIndex;
    }

    return r;
  }
}

const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
let output = []; // 결과 출력을 위한 배열

readline.on("line", (line) => {
  if (line.trim() === "") {
    readline.close();
  } else {
    input.push(line);
  }
});

readline.on("close", () => {
  const N = input[0];
  const heap = new MinHeap();
  for (let i = 1; i <= N; i++) {
    if (input[i] == 0) {
      output.push(heap.pop());
    } else {
      heap.insert(parseInt(input[i]));
    }
  }
  console.log(output.join("\n"));
  process.exit();
});
