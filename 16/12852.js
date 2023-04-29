const fs = require('fs');
// const input = fs.readFileSync('12852.txt').toString().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
let [n] = input[0].split(' ').map((e) => parseInt(e));

let result = n + 1;
let resultArr = [];
function go(num, cnt, arr) {
  if (cnt >= result) return;
  if (num === 1) {
    if (result > cnt) {
      result = cnt;
      resultArr = [...arr];
    }
    return;
  }
  if (num % 3 === 0)
    go(parseInt(num / 3), cnt + 1, [...arr, parseInt(num / 3)]);
  if (num % 2 === 0)
    go(parseInt(num / 2), cnt + 1, [...arr, parseInt(num / 2)]);
  go(num - 1, cnt + 1, [...arr, num - 1]);
}
go(n, 0, [n]);
console.log(result);
console.log(resultArr.join(' '));
