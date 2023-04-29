const fs = require('fs');
// const input = fs.readFileSync('2623.txt').toString().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
let [n, m] = input[0].split(' ').map((i) => parseInt(i));
let coms = [];
for (let i = 1; i < m + 1; i++) {
  coms.push(
    input[i]
      .split(' ')
      .map((i) => parseInt(i))
      .slice(1)
  );
}

let g = [];
Array.from({ length: n + 1 }).forEach(() => g.push(new Set()));
let degrees = Array(n + 1).fill(0);
for (let com of coms) {
  for (let i = 1; i < com.length; i++) {
    if (!g[com[i - 1]].has(com[i])) {
      g[com[i - 1]].add(com[i]);
      degrees[com[i]] += 1;
    }
  }
}

let q = [];
for (let i = 1; i < degrees.length; i++) {
  if (degrees[i] === 0) {
    q.push(i);
  }
}

let result = [];
while (q.length) {
  let cur = q.shift();
  result.push(cur);
  for (let next of g[cur]) {
    degrees[next] -= 1;
    if (degrees[next] === 0) q.push(next);
  }
}

if (result.length !== n) console.log(0);
else result.forEach((e) => console.log(e));
