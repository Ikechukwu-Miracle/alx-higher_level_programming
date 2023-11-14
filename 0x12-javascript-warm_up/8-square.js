#!/usr/bin/node

if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  const numSize = Number(process.argv[2]);
  for (let i = 0; i < numSize; i++) {
    console.log('X'.repeat(numSize));
  }
}
