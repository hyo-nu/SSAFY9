const threeArgs = function (arg1, arg2, arg3) {
  return [arg1, arg2, arg3];
};

threeArgs;

const restArgs = function (arg1, arg2, ...restArgs) {
  return [arg1, arg2, restArgs];
};

console.log(restArgs(1, 2, 3, 4, 5));

console.log("============================");

// Arrow function
const arrow1 = function (name) {
  return `hello ${name}`;
};

// 1. function 키워드 생략 가능
const arrow2 = (name) => {
  return `hello ${name}`;
};

// 2. 인자가 1개인 경우에만 () 생략 가능
const arrow3 = (name) => {
  return `hello ${name}`;
};

// 3. 함수 바디가 return을 포함한 표현식 1개일 경우에 {} & ruturn 삭제 가능
const arrow4 = (name) => `hello ${name}`;

console.log("============================");

const colors = ["red", "blue", "green"];

printFunc = function (color) {
  console.log(color);
};

colors.forEach(printFunc);
console.log();
``;
colors.forEach(function (color, index, array) {
  console.log(color);
  console.log(index);
  console.log(array);
});

// array.forEach((element) => {
//   return console.log(color);
// });

// map
console.log("============================");

const numbers = [1, 2, 3];

const doubleFunc = function (number) {
  return number * 2;
};

// const doubleNumbers = number.map(doubleFunc)
// console.log(doubleNumbers)

const doubleNumbers = numbers.map(function (number) {
  return number * 2;
});
console.log(doubleNumbers);

//filer
console.log("============================");

const products = [
  { name: "cucuber", type: "vegat" },
  { name: "banana", type: "fruit" },
  { name: "carrot", type: "veget" },
  { name: "apple", type: "fruit" },
];

const fruitFilter = function (product) {
  return product.type === "fruit";
};

const fruits = products.filter(fruitFilter);
console.log(fruits);

//reduce
console.log("============================");

const tests = [90, 90, 80, 77];

const sum = tests.reduce(function (total, x) {
  return total + x;
}, 0);
//total이 acc버튼 , x가 element요소

console.log(sum);

const key = "나라";
const value = ["ab", "asdb", "asdfwe", "asde"];

const myObj = {
  [key]: value,
};

console.log(myObj);
console.log(myObj.나라);
console.log(myObj.나라[2]);

console.log("==================================================");

const userInformation = {
  name: "ssafy jeong",
  USerId: "ssasdf1234",
  email: "gusehd502@nave.com",
};
const { name } = userInformation;
const { USerId } = userInformation;
const { email } = userInformation;

console.log(name);
console.log(USerId);
console.log(email);
