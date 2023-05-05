const fs = require('fs');
// const input = fs.readFileSync('21611.txt').toString().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [n, m] = input[0].split(' ').map((i) => parseInt(i));
const g = [[]];
const g1 = [[]];
const result = [0, 0, 0, 0];
for (let i = 1; i <= n; i++) {
  g.push([0, ...input[i].split(' ').map((i) => parseInt(i))]);
  g1.push(new Array(n + 1));
}
const com = [];
for (let i = n + 1; i < n + m + 1; i++) {
  com.push(input[i].split(' ').map((i) => parseInt(i)));
}
let start = [parseInt(n + 1) / 2, parseInt(n + 1) / 2];
g1[start[0]][start[1]] = 0;
let cnt = 0;
let cnt1 = 0;
let i = 1;
let di = [
  [0, -1],
  [1, 0],
  [0, 1],
  [-1, 0],
];

function inRange(y, x) {
  return 1 <= y && y <= n && 1 <= x && x <= n;
}

while (true) {
  let flag = false;
  let tmp = [start[0], start[1]];
  for (let j = 1; j <= i; j++) {
    const ny = start[0] + di[cnt % 4][0] * j;
    const nx = start[1] + di[cnt % 4][1] * j;
    if (!inRange(ny, nx)) {
      flag = true;
      break;
    }
    tmp = [ny, nx];
    cnt1 += 1;
    g1[ny][nx] = cnt1;
  }
  if (flag) break;
  start = [tmp[0], tmp[1]];
  if (cnt % 2) {
    i += 1;
  }
  cnt += 1;
}

let stack = new Array(n * n).fill(0);
for (let i = 1; i <= n; i++) {
  for (let j = 1; j <= n; j++) {
    stack[g1[i][j]] = g[i][j];
  }
}

function move() {
  let tmp = [0];
  for (let i = 1; i < n * n; i++) {
    if (stack[i] !== 0) {
      tmp.push(stack[i]);
    }
  }
  stack = new Array(n * n).fill(0);
  for (let i = 1; i < tmp.length; i++) {
    stack[i] = tmp[i];
  }
}

function boom() {
  let flag = false;
  let i = 1;
  let j = 1;
  while (i < n * n) {
    if (stack[i] === 0) break;
    while (true) {
      if (stack[i] !== stack[j]) break;
      j += 1;
    }
    if (j - i >= 4) {
      flag = true;
      result[stack[i]] += j - i;
      for (let k = i; k < j; k++) {
        stack[k] = 0;
      }
    }
    i = j;
  }
  return flag;
}

function make() {
  let i = 1;
  let j = 1;
  let tmp = [];
  while (i < n * n) {
    if (stack[i] === 0) break;
    while (true) {
      if (stack[i] !== stack[j]) break;
      j += 1;
    }
    let tmp1 = [];
    for (let k = i; k < j; k++) {
      tmp1.push(stack[k]);
    }
    tmp.push(tmp1);
    i = j;
  }
  return tmp;
}

di = [[], [-1, 0], [1, 0], [0, -1], [0, 1]];

for (let i = 0; i < m; i++) {
  let [d, s] = com[i];
  for (let j = 1; j <= s; j++) {
    let [dy, dx] = di[d];
    let ny = parseInt(n + 1) / 2 + dy * j;
    let nx = parseInt(n + 1) / 2 + dx * j;
    if (inRange(ny, nx)) {
      stack[g1[ny][nx]] = 0;
    }
  }
  move();
  while (boom()) move();
  let tmp = [0];
  for (e of make()) {
    tmp.push(e.length);
    tmp.push(e[0]);
  }
  for (let j = 1; j < n * n; j++) {
    if (tmp[j] === undefined) {
      stack[j] = 0;
    } else {
      stack[j] = tmp[j];
    }
  }
}
console.log(result[1] + 2 * result[2] + 3 * result[3]);
