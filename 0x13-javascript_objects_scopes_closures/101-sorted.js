#!/usr/bin/node
const dict = require('./101-data').dict;

const totalL = Object.entries(dict);
const vs = Object.values(dict);
const uniqVals = [...new Set(vs)];
const newDict = {};
for (const j in uniqVals) {
  const list = [];
  for (const k in totalL) {
    if (totalL[k][1] === uniqVals[j]) {
      list.unshift(totalL[k][0]);
    }
  }
  newDict[uniqVals[j]] = list;
}
console.log(newDict);
