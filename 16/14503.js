const fs = require('fs');
// const input = fs.readFileSync('14503.txt').toString().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const di = [
  [-1, 0],
  [0, 1],
  [1, 0],
  [0, -1],
];
const [n, m] = input[0].split(' ').map((i) => parseInt(i));
let [r, c, d] = input[1].split(' ').map((i) => parseInt(i));
const g = [];
let result = 0;
for (let i = 2; i < n + 2; i++) {
  g.push(input[i].split(' ').map((i) => parseInt(i)));
}

function rotate() {
  if (d === 0) {
    d = 3;
  } else {
    d -= 1;
  }
}

function cleanAndCheck(y, x) {
  if (g[y][x] === 0) {
    result += 1;
    g[y][x] = 2;
  }
  let flag = false;
  for (const [dy, dx] of di) {
    const ny = y + dy;
    const nx = x + dx;
    if (g[ny][nx] === 0) {
      flag = true;
    }
  }
  return flag;
}

while (true) {
  if (cleanAndCheck(r, c)) {
    while (true) {
      rotate();
      const [dy, dx] = di[d];
      const ny = r + dy;
      const nx = c + dx;
      if (g[ny][nx] === 0) {
        r = ny;
        c = nx;
        break;
      }
    }
  } else {
    const [dy, dx] = di[d];
    const ny = r - dy;
    const nx = c - dx;
    if (g[ny][nx] === 1) {
      break;
    } else {
      r = ny;
      c = nx;
    }
  }
}

console.log(result);
