#!/usr/bin/node
// script that prints x times “C is fun”

const numXoccur = parseInt(process.argv[2]);
if (isNaN(numXoccur)) {
  console.log('Missing number of occurences');
} else {
  let i;
  for (i = 0; i < numXoccur; i++) {
    console.log('C is fun');
  }
}
