#!/usr/bin/node

/*script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer*/
const arg = process.argv[2];
const num = parseInt(arg);

if (Number.isNaN(num)) {
  console.log("Not a number");
} else {
  console.log(`My number: ${num}`);
}
