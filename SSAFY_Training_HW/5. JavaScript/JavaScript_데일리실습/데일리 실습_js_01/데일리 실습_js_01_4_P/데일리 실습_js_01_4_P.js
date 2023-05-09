const p1 = [
  "rock",
  "paper",
  "scissors",
  "scissors",
  "rock",
  "rock",
  "paper",
  "paper",
  "rock",
  "scissors",
];
const p2 = [
  "paper",
  "paper",
  "rock",
  "scissors",
  "paper",
  "scissors",
  "scissors",
  "rock",
  "rock",
  "rock",
];

const RSP = {
  rock: 0,
  scissors: 1,
  paper: 2,
};
const playGame = (p1_choice, p2_choice) => {
  for (let i = 0; i < p1.length; i++) {
    win = RSP[p1_choice[Number(i)]] - RSP[p2_choice[Number(i)]];
    if (win === -1 || win === 2) {
      console.log(1);
    } else if (win === 1 || win === -2) {
      console.log(2);
    } else {
      console.log(0);
    }
  }
};
console.log(playGame(p1, p2));
// 2
// 0
// 2
// 0
// 2
// 1
// 2
// 1
// 0
// 2
