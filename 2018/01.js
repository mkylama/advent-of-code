const fs = require('fs');

var raw_input = fs.readFileSync('input/01.txt','utf8').trim();

var input = raw_input.split("\n");

// 0101 --------------------------------------------------

console.log('0101:',input.reduce(function(t,n){return parseInt(t)+parseInt(n)},0));

// 0102 --------------------------------------------------

var freqs = [];
var found = false;
var start = 0;

while (!found) {
	start = input.reduce(function(t,n){
		var temp = parseInt(t)+parseInt(n);
		if (freqs.indexOf(temp) > -1 && !found) {
			console.log('0102:',temp);
			found = true
		} else {
			freqs.push(temp);
			return temp;
		}
	},start);
}