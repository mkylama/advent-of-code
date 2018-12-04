const fs = require('fs');

var raw_input = fs.readFileSync('input/04.txt','utf8').trim();

var input = raw_input.split("\n");

input.sort();

var guards = {};

var current_guard = null;
var asleep = null;

// 0401 --------------------------------------------------

for (i of input) {
	var split = i.split(' ');
	if (split[2] == 'Guard') {
		current_guard = split[3].substr(1);
		if (!(current_guard in guards)) {
			guards[current_guard] = new Array(60).fill(0);
		}
	} else if (split[2] == 'falls') {
		asleep = parseInt(split[1].split(':')[1].substr(0,2));
	} else if (split[2] == 'wakes') {
		var wake = parseInt(split[1].split(':')[1].substr(0,2));
		for (var m = asleep; m < wake; m++) {
			guards[current_guard][m]++;
		}
	}
}

var maxduration = 0;
var guardid = null;

for (g in guards) {
	var total = guards[g].reduce(function(num, total) { return num + total; }, 0);
	if (total > maxduration) {
		maxduration = total;
		guardid = g;
	}
}

console.log('0401:',guards[guardid].indexOf(Math.max(...guards[guardid]))*guardid);

// 0402 --------------------------------------------------

var maxcount = 0;

for (g in guards) {
	total = Math.max(...guards[g]);
	if (total > maxcount) {
		maxcount = total;
		guardid = g;
	}
}

console.log('0402:',guards[guardid].indexOf(Math.max(...guards[guardid]))*guardid);