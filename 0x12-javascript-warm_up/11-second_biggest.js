#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  let i;
  let max = parseInt(process.argv[2]);
  let second = parseInt(process.argv[2]);
  for (i = 3; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > max) {
      max = parseInt(process.argv[i]);
    }
  }
  if (second === max) {
    second = parseInt(process.argv[3]);
  }
  for (i = 3; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > second && parseInt(process.argv[i]) < max) {
      second = parseInt(process.argv[i]);
    }
  }
  console.log(second);
}
