// function hello() {
//   console.log("hello");
// }

// function func(callback) {
//   callback();
// }

// func(hello);

// function func(callback) {
//   callback("우후~");
// }
// func(function (msg) {
//   console.log("hello" + msg);
// });

// let hello = function () {
//   console.log("hello!");
// };

// //function 키워드 삭제하고,
// hello = () => {
//   console.log("hello!");
// };

// hello = () => console.log("hello!");

// map
// const nums = [1, 2, 3, 4, 5];
// let double_nums = [];
// const ret = nums.map(function (val) {
//   double_nums.push(val * 2);
//   return val ** 2;
// });
// console.log(ret);
// console.log(double_nums);

// const nums = [1, 2, 3, 4, 5];
// const ret = nums.filter(function (val) {
//   return val % 2 === 0;
// });
// console.log(ret);

function callback(prev, cur) {
  prev.push(cur ** 2);
  console.log(prev);

  return prev;
}
const nums = [1, 2, 3, 4, 5];
const ret = nums.reduce(callback, []);
console.log(ret);
