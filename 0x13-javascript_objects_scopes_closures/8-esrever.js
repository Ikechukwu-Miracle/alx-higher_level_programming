#!/usr/bin/node

exports.esrever = function (list) {
  let n = (list.length - 1);
  let i = 0;

  while ((n - 1) > 0) {
    const temp = list[n];
    list[n] = list[i];
    list[i] = temp;
    i++;
    n--;
  }

  return list;
};
