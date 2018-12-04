const fs = require('fs');

var raw_input = fs.readFileSync('input/01.txt','utf8').trim();

var input = raw_input.split("\n");

// 0101 --------------------------------------------------

console.log('0101:',input.reduce(function(t,n){return parseInt(t)+parseInt(n)},0));

// 0102 --------------------------------------------------

var freqs = [];
var found = false;
var freq = 0;

while (!found) {
	for (i of input) {
		freq += parseInt(i);
		if (freqs.indexOf(freq) > -1) {
			found = true;
			break;
		}
		freqs.push(freq);
	}
}

console.log('0102:',freq);