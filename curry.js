// const addCustomer =
//   (fn) =>
//   (...args) => {
//     console.log("Adding customer...");
//     return fn(...args);
//   };

// const processOrder =
//   (fn) =>
//   (...args) => {
//     console.log(`Processing order... ${args[0]}`);
//     return fn(...args);
//   };

// let completeOrder = (...args) => {
//   console.log(`Completing order... ${[...args].toString()}`);
// };

// completeOrder = processOrder(completeOrder);
// completeOrder = addCustomer(completeOrder);
// completeOrder("1000");

// function addCustomer(...args) {
//   console.log("Adding customer...");
//   return function processOrder(...args) {
//     console.log(`Processing order... ${args[0]}`);
//     return function completeOrder(...args) {
//       console.log(`Completing order... ${[...args].toString()}`);
//     };
//   };
// }

// console.log(addCustomer("1000")("1000")("1000"));

const curry = (fn) => {
  return function curried(...args) {
    console.log("args.length =", args.length);
    if (args.length !== fn.length) {
      return curried.bind(null, ...args);
    }
    return fn(...args);
  };
};

const add = (a, b, c) => a + b + c;

const curriedAdd = curry(add);
console.log(curriedAdd(1)(2)(3));
