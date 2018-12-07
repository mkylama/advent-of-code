const fs = require('fs');

var raw_input = fs.readFileSync('input/06.txt','utf8').trim();

var input = raw_input.split("\n").map(function(i){ s = i.split(', '); return [parseInt(s[0]),parseInt(s[1])]});

// 0601 & 0602 -------------------------------------------

var x_min = Math.min.apply(Math, input.map(function(x) {return x[0]}));
var x_max = Math.max.apply(Math, input.map(function(x) {return x[0]}));
var y_min = Math.min.apply(Math, input.map(function(y) {return y[1]}));
var y_max = Math.max.apply(Math, input.map(function(y) {return y[1]}));

var part2 = 0;

var grid = new Array(input.length).fill(0);

for (var y = y_min; y <= y_max; y++) {
	for (var x = x_min; x <= x_max; x++) {
		var total_dist = 0;
		var min_dist = 99999;
		var closest = '.';
		for (i in input) {
			dist = Math.abs(x - input[i][0])+Math.abs(y - input[i][1]);
			// 01
			if (dist == min_dist) {
				closest = '.';
			} else if (dist < min_dist) {
				closest = i;
				min_dist = dist;
			}
			// 02
			total_dist += dist;
		}
		// 01
		if (x == x_min || x == x_max || y == y_min || y == y_max)
			grid[closest] = null;
		else if (closest != '.' && grid[closest] != null)
			grid[closest]++;
		// 02
		if (total_dist < 10000) part2++;
	}
}

console.log('0601:',Math.max(...grid));

console.log('0602:',part2);