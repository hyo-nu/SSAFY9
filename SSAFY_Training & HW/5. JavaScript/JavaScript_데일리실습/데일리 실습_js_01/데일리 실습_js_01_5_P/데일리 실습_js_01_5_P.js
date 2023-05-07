const participantNums = [
  [1, 3, 2, 2, 1],
  [3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
  [9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35],
];

for (const key of participantNums) {
  key.sort();
  key.push(0);
  for (let i = 0; i < key.length - 1; i += 2) {
    if (key[Number(i)] !== key[Number(i + 1)]) {
      result = key[Number(i)];
      break;
    }
  }
  console.log(result);
}

// 3
// 100
// 62
