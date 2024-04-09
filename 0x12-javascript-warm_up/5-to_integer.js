#!/usr/bin/node
// script that prints My number:

const arg = parseInt(process.argv[2], 10);

if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${arg}`);
}
