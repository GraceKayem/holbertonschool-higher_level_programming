#!/usr/bin/node
/* Script that prints 3 lines using an array and a loop */

const languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let output = '';

for (let i = 0; i < languages.length; i++) {
  output += languages[i] + '\n';
}

console.log(output.trim());
