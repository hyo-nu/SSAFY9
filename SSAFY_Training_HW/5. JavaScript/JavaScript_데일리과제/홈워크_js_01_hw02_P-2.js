const nums = [1, 2, 3, 4]

const squareFunc = function (num){
  return num ** 3
}

const squareNums = nums.map(squareFunc)
console.log(squareNums)