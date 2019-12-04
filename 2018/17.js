const fs = require('fs');

var raw_input = fs.readFileSync('input/17.txt','utf8').trim();

var input = raw_input.split("\n");

// 1701 & 1702 -------------------------------------------

var x_min = null, x_max = null, y_min = null, y_max = null;

var walls = [];

function addWall(x,y) {
	if (x_min == null || x < x_min)
		x_min = x;
	if (x_max == null || x > x_max)
		x_max = x;
	if (y_min == null || y < y_min)
		y_min = y;
	if (y_max == null || y > y_max)
		y_max = y;
	var wall = x+','+y;
	if (walls.indexOf(wall) == -1)
		walls.push(wall);
}

for (i of input) {
	var numbers = i.match(/[0-9]+/g).map(function(n){return parseInt(n)});
	for (var n = numbers[1]; n <= numbers[2]; n++) {
		if (i.charAt(0) == 'y')
			addWall(n,numbers[0]);
		else
			addWall(numbers[0],n);
	}
}

x_min--;
x_max++;

var ground = new Array(y_max+1).fill('.').map(function(n){return new Array(x_max-x_min+1).fill('.')});

ground[0][500-x_min] = '+';
water_reach = 0;
water_still = 0;

for (w of walls) {
	var c = w.split(',').map(function(n){return parseInt(n)});
	ground[c[1]][c[0]-x_min] = '#';
}

function water(x,y) {
	ground[y][x] = '|';
	if (y < y_max) {
		if (ground[y+1][x] == '.') {
			water(x,y+1);
		}
		if (ground[y+1][x] == '#' || ground[y+1][x] == '~') {
			// find left
			var left = x;
			var left_wall = false;
			for (var tx = x; tx >= 0; tx--) {
				if (tx - 1 > 0 && ground[y][tx - 1] == '#') {
					left = tx;
					left_wall = true;
					break;
				} else if (y < y_max && ground[y+1][tx] == '.') {
					left = tx;
					break;
				}
			}

			// find right
			var right = x;
			var right_wall = false;
			for (var tx = x; tx < x_max - x_min; tx++) {
				if (tx + 1 < x_max - x_min && ground[y][tx + 1] == '#') {
					right = tx;
					right_wall = true;
					break;
				} else if (y < y_max && ground[y+1][tx] == '.') {
					right = tx;
					break;
				}
			}

			if (left_wall && right_wall) {
				for (var tx = left; tx <= right; tx++)
					ground[y][tx] = '~';
			} else {
				for (var tx = left; tx <= right; tx++)
					ground[y][tx] = '|';
			}

			if (!left_wall)
				water(left,y);
			if (!right_wall)
				water(right,y);
		}
	}
}

function render() {
	for (y of ground)
		console.log(y.join(''));
}

water(500-x_min,1);

for (var y = y_min; y < ground.length; y++) {
	for (var x = 0; x < ground[y].length; x++) {
		if (ground[y][x] == '~') {
			water_reach++;
			water_still++;
		}
		if (ground[y][x] == '|')
			water_reach++;
	}
}

//render();

console.log('0701:',water_reach);

console.log('0702:',water_still);