const n = 4;
const g = [
  [5, 3],
  [3, 2],
  [2, 6],
  [6, 4],
];

function solution(n, g) {
  const dp = Array.from({ length: n }).map(() =>
    Array.from({ length: n }).fill(-1)
  );

  for (let i = 0; i < n; i++) {
    dp[i][i] = 0;
  }

  function go(start, end) {
    if (dp[start][end] !== -1) {
      return dp[start][end];
    }

    let result = 10 ** 9;
    for (let mid = start; mid < end; mid++) {
      const tmp =
        go(start, mid) + go(mid + 1, end) + g[start][0] * g[mid][1] * g[end][1];
      result = Math.min(result, tmp);
    }

    dp[start][end] = result;
    return result;
  }

  return go(0, n - 1);
}

console.log(solution(n, g));
