const fs = require('fs');

var input = parseInt(fs.readFileSync('input/11.txt','utf8').trim());

ainput = 18;

// 1101 & 1102 -------------------------------------------

var grid = [];

var size = 300;

for (var x = 0; x < size; x++) {
	grid[x] = [];
	for (var y = 0; y < size; y++) {
		var power_level = Math.floor( (((((x + 1) + 10) * (y + 1) + input) * ((x + 1) + 10)) % 1000) / 100) - 5;
		grid[x].push(power_level);
	}
}

var summed = grid;

for (var i=0; i<size; i++) 
	summed[0][i] = grid[0][i]; 

for (var i=1; i<size; i++) 
	for (var j=0; j<size; j++) 
		summed[i][j] = grid[i][j] + summed[i-1][j]; 

	for (var i=0; i<size; i++) 
		for (var j=1; j<size; j++) 
			summed[i][j] += summed[i][j-1];

function areaSum(x1,y1,x2,y2) {
	var sum = summed[x2][y2];

	if (x1 > 0)
		sum = sum - summed[x1-1][y2]; 

	if (y1 > 0) 
		sum = sum - summed[x2][y1-1]; 

	if (x1 > 0 && y1 > 0) 
		sum = sum + summed[x1-1][y1-1]; 

	return sum; 
}

function find(min_area,max_area) {
	var max = 0;
	var max_id = [null,null];

	for (var s = min_area-1; s < max_area; s++) {
		for (var x = 0; x < size - s; x++) {
			for (var y = 0; y < size - s; y++) {
				var total = areaSum(x,y,x+s,y+s);
				if (total > max) {
					max = total;
					max_id = [(x+1)+','+(y+1),(s+1)];
				}
			}
		}
	}
	return max_id;
}

var part1 = find(3,3);
console.log('1101:',part1[0]);

var part2 = find(1,300);
console.log('1102:',part2[0]+','+part2[1]);