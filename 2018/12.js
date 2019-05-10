const fs = require('fs');

var raw_input = fs.readFileSync('input/12.txt','utf8').trim();

araw_input = `initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #`;

var input = raw_input.split("\n");

// 1201 & 1102 -------------------------------------------

var notes = {};

var plants = input[0].split(' ')[2];

var start_index = 0;

for (var i = 2; i < input.length; i++) {
	var s = input[i].split(' => ');
	notes[s[0]] = s[1];
}

function generation(plants,g) {
	while (plants.charAt(0) == '#' || plants.charAt(1) == '#' || plants.charAt(2) == '#' || plants.charAt(3) == '#') {
		plants = '.'+plants;
		start_index--;
	}
	while (plants.charAt(plants.length-1) == '#' || plants.charAt(plants.length-2) == '#' || plants.charAt(plants.length-3) == '#' || plants.charAt(plants.length-4) == '#') {
		plants += '.';
	}
	var new_plants = plants;
	for (var p = 2; p < plants.length - 2; p++) {
		var seq = plants.substr(p-2,5);
		if (seq in notes) {
			new_plants = new_plants.substring(0, p) + notes[seq] + new_plants.substring(p+1);
		} else {

			new_plants = new_plants.substring(0, p) + '.' + new_plants.substring(p+1);
		}
	}
	console.log(g,start_index,sum(plants,start_index));
	return new_plants;
}

function sum(plants,start_index) {
	var res = 0;

	for (var i = 0; i < plants.length; i++) {
		if (plants.charAt(i) == '#')
			res += i + start_index;
	}
	return res;
}

for (var g = 0; g < 20; g++) {
	plants = generation(plants,g);
}

console.log('1201:',sum(plants,start_index));

var part2 = 110475;

console.log('1202:',110475 + (50000000000-5000)*22);