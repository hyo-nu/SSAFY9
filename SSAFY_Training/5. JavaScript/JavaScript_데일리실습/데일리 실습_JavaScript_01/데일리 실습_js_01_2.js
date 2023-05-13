words = ["level", "noon", "mom", "happy", "ssafy", "life"];

function palindrome(word) {
  for (let i = 0; i < word.length / 2; i++) {
    if (word[i] !== word[word.length - 1 - i]) {
      return false;
    }
  }
  return true;
}

for (const word of words) {
  console.log(palindrome(word));
}

// 출력 예시
// true
// true
// true
// false
// false
// false
