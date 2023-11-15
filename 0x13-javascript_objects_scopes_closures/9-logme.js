#!/usr/bin/node
let numArg = 0;

exports.logMe = function (item) {
  const printOut = numArg + ': ' + item;
  console.log(printOut);
  numArg++;
};