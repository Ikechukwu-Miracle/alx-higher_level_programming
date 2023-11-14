#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Not a number');
} else {
  const myNumber = parseInt(process.argv[2]);
  console.log('My number:', myNumber);
}
