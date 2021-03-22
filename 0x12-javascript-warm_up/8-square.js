#!/usr/local/bin/node
let i;
let xtring = '';
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (i = 0; i < parseInt(process.argv[2]); i++) {
    xtring = xtring + 'X';
  }
  for (i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(xtring);
  }
}
