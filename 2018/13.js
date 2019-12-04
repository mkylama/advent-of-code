const fs = require('fs');

var raw_input = fs.readFileSync('input/13_test.txt','utf8');

var input = raw_input.split("\n").map(function(i){
	return i.replace("\r",'').split('');
});

// 1301 & 1302 -------------------------------------------


var trains = [];
var crash = false;

var turning = ['^','>','v','<'];

// collect trains
for (var y = 0; y < input.length; y++) {
	for (var x = 0; x < input[y].length; x++) {
		if (turning.includes(input[y][x])) {
			trains.push({'dir':input[y][x],'is':0,'x':x,'y':y})
			if (['^','v'].includes(input[y][x]))
				input[y][x] = '|';
			else
				input[y][x] = '-';
		}
	}
}

//console.log(trains)

function train_sorter(a,b) {
	if (a['y'] < b['y'])
		return -1;
	if (a['y'] > b['y'])
		return 1;
	if (a['x'] < b['x'])
		return -1;
	if (a['x'] > b['x'])
		return 1;
	return 0;
}

function train_move(train) {
	var ny = train['y'], nx = train['x'];
	if (train['dir'] == '^')
		train['y']--;
	else if (train['dir'] == '>')
		train['x']++;
	else if (train['dir'] == 'v')
		train['y']++;
	else if (train['dir'] == '<')
		train['x']--;

	var track = input[train['y']][train['x']];
	if (track == '/') {
		if (train['dir'] == '^')
			train['dir'] = '>';
		else if (train['dir'] == '>')
			train['dir'] = '^';
		else if (train['dir'] == 'v')
			train['dir'] = '<';
		else if (train['dir'] == '<')
			train['dir'] = 'v';
	} else 	if (track == '\\') {
		if (train['dir'] == '^')
			train['dir'] = '<';
		else if (train['dir'] == '>')
			train['dir'] = 'v';
		else if (train['dir'] == 'v')
			train['dir'] = '>';
		else if (train['dir'] == '<')
			train['dir'] = '^';
	} else if (track == '+') {
		train_turn(train);
	}
	// check crash
	let seen = new Set();
	if (trains.some(function(train) {
		return seen.size === seen.add(train['x']+','+train['y']).size;
	})) {
		console.log('1301:',train['x']+','+train['y']);
		crash = true;
	}
}

function train_turn(train) {
	var i = turning.indexOf(train['dir']);
	var c = train['is'] % 3;
	if (c == 0)
		i--;
	else if (c == 2)
		i++;
	if (i < 0)
		i += 4;
	if (i > 3)
		i -= 4
	train['dir'] = turning[i];
	train['is']++;
}

function printer(image) {
	for (train of trains) {
		image[train['y']][train['x']] = train['dir'];
	}
	for (var y = 0; y < image.length; y++) {
		console.log(image[y].join(''))
	}
}

var iter = 0;

while (!crash) {
	console.log(iter++);
	printer(JSON.parse(JSON.stringify(input)));
	for (train of trains) {
		train_move(train);
		if (crash)
			break;
	}
	trains.sort(train_sorter);
}

console.log(trains);