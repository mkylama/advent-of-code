const fs = require('fs');

var raw_input = fs.readFileSync('input/02.txt','utf8').trim();

var input = raw_input.split("\n");

// 0201 --------------------------------------------------

var doubles = 0;
var triples = 0;

for (i of input) {
	var counter = [];
	for (s of i.split('')) {
		if (counter[s] == undefined)
			counter[s] = 1;
		else
			counter[s]++;	
	}
	if (Object.values(counter).includes(2))
		doubles++;
	if (Object.values(counter).includes(3)) 
		triples++;
}

console.log('0201:',doubles*triples);

// 0202 --------------------------------------------------

input.sort();

for (var i = 0; i < input.length-1; i++) {
	var differences = 0;
	var d_index = null;
	for (var s = 0; s < input[i].length; s++) {
		if (input[i].charAt(s) != input[i+1].charAt(s)) {
			differences++;
			d_index = s;
		}
		if (differences > 1)
			break;
	}
	if (differences == 1) {
		console.log('0202:',input[i].substr(0,d_index)+input[i].substr(d_index+1));
		break;
	}
}