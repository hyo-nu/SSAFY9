const inputs = [
  [3, 10, 5, [1, 3, 5, 7, 9]], // 3
  [3, 10, 5, [1, 3, 7, 8, 9]], // 0
  [5, 20, 5, [4, 7, 9, 14, 17]], // 4
];

function solution(K, N, M, chargers) {
  let start = 0;
  let charge = 0;
  while (start < N) {
    now = start;
    start += K;
    if (start >= N) {
      return charge;
    }
    for (let i = 0; i < 3; i++) {
      if (chargers.includes(start)) {
        charge += 1;
        break;
      }
      start -= 1;
    }
    if (now === start) {
      return 0;
    }
  }
  return charge;
}

for (const input of inputs) {
  charge = solution(input[0], input[1], input[2], input[3]);
  console.log("#" + charge);
}
