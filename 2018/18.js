const fs = require('fs');

var raw_areas = fs.readFileSync('input/18.txt','utf8');

var areas = raw_areas.split("\n").map(function(i){
	return i.replace("\r",'').split('');
});

// 1801 & 1802 -------------------------------------------

function change(areas) {
	new_areas = JSON.parse(JSON.stringify(areas));
	var surrounding = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]];

	for (var y = 0; y < areas.length; y++) {
		for (var x = 0; x < areas[y].length; x++) {
			var open = 0;
			var trees = 0;
			var lumber = 0;
			for (s of surrounding) {
				if (x + s[1] >= 0 && x + s[1] < areas[y].length && y + s[0] >= 0 && y + s[0] < areas.length) {
					area = areas[y+s[0]][x+s[1]];
					if (area == '.')
						open++;
					else if (area == '|')
						trees++;
					else if (area == '#')
						lumber++;
				}
			}
			if (areas[y][x] == '.' && trees >= 3) {
				new_areas[y][x] = '|';
			} else if (areas[y][x] == '|' && lumber >= 3) {
				new_areas[y][x] = '#';
			} else if (areas[y][x] == '#' && (lumber < 1 || trees < 1)) {
				new_areas[y][x] = '.';
			}
		}
	}
	return JSON.parse(JSON.stringify(new_areas));
}

function printer() {
	console.log('')
	for (row of areas) {
		console.log(row.join(''));
	}
}

function value() {
	trees = 0;
	lumber = 0;
	for (var y = 0; y < areas.length; y++) {
		for (var x = 0; x < areas[y].length; x++) {
			if (areas[y][x] == '|')
				trees++;
			else if (areas[y][x] == '#')
				lumber++;
		}
	}
	return trees * lumber;
}

for (var i = 1; i <= 608; i++) {
	areas = change(areas);
	if (i == 10)
		console.log('1801:',value());
}

// manually found the repeating pattern and checked "minutes" for the first occurance (608)
console.log('1802:',value());