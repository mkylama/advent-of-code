const fs = require('fs');

var raw_input = fs.readFileSync('input/03.txt','utf8').trim();

var input = raw_input.split("\n");

// 0301 --------------------------------------------------

var fabric = {};

var overlap = 0;

var overlapping = {};

var clear = null;

for (i of input) {
	var numbers = i.match(/[0-9]+/g);
	overlapping[parseInt(numbers[0])] = 1;
	for (var x = parseInt(numbers[1]); x < parseInt(numbers[1]) + parseInt(numbers[3]); x++) {
		for (var y = parseInt(numbers[2]); y < parseInt(numbers[2]) + parseInt(numbers[4]); y++) {
			if (x+'x'+y in fabric) {
				if (fabric[x+'x'+y].length == 1)
					overlap++;
				fabric[x+'x'+y].push(parseInt(numbers[0]));
			} else {
				fabric[x+'x'+y] = [parseInt(numbers[0])];
			}
		}
	}
}

console.log('0301:',overlap);

// 0302 --------------------------------------------------

for (var s in fabric) {
	if (fabric[s].length > 1) {
		for (n of fabric[s]) {
			//console.log(n)
			delete overlapping[n];
		}
	}
}

console.log('0302:',Object.keys(overlapping)[0]);