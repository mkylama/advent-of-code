const fs = require('fs');

var raw_input = fs.readFileSync('input/13_test.txt','utf8');

var input = raw_input.split("\n").map(function(i){
	return i.replace("\r",'').split('');
});

// 1301 & 1302 -------------------------------------------

var crash = false;
var iteration = 0;

var turning = ['^','>','v','<'];

function train_check(x,y) {
	if (['<','>','^','v'].includes(input[y][x])) {
		var track = '|';
		if (['<','>'].includes(input[y][x]))
			track = '-';
		input[y][x] = [input[y][x],0,track,-1];
		console.log('init train',x,y,input[y][x])

	}
	if (typeof input[y][x] == 'object' && input[y][x][3] !== iteration) {
		train_move(x,y);
	}
}

function train_move(x,y) {
	var direction = input[y][x][0];
	console.log('dir',direction);
	var nx = x, ny = y;
	if (direction == '^') {
		ny--;
	} else if (direction == '>') {
		nx++;
	} else if (direction == 'v') {
		ny++;
	} else if (direction == '<') {
		nx--;
	}
	if (typeof input[ny][nx] == 'object') {
		console.log('found')
		crash = true;
		console.log('1301',x+','+y);
	} else {
		var track = input[ny][nx];
		console.log('track',track)
		input[ny][nx] = [input[y][x][0],input[y][x][1],track,iteration];
	}
	if (input[ny][nx][2] == '/') {
		if (input[ny][nx][0] == '^')
			input[ny][nx][0] = '>';
		else if (input[ny][nx][0] == '>')
			input[ny][nx][0] = '^';
		else if (input[ny][nx][0] == 'v')
			input[ny][nx][0] = '<';
		else if (input[ny][nx][0] == '<')
			input[ny][nx][0] = 'v';
	} else if (input[ny][nx][2] == '\\') {
		if (input[ny][nx][0] == '^')
			input[ny][nx][0] = '>';
		else if (input[ny][nx][0] == '>')
			input[ny][nx][0] = 'v';
		else if (input[ny][nx][0] == 'v')
			input[ny][nx][0] = '>';
		else if (input[ny][nx][0] == '<')
			input[ny][nx][0] = '^';
	} else if (input[ny][nx][2] == '\\'){
		input[ny][nx] = turn(input[ny][nx][0]);
	}
	input[y][x] = input[y][x][2];
}

function train_turn(train) {
	console.log(train)
	var i = turning.indexOf(train[0]);
	var c = train[1] % 3;
	console.log('c',c)
	if (c == 0)
		i--;
	else if (c == 2)
		i++;
	if (i < 0)
		i += 4;
	if (i > 3)
		i -= 4
	train[0] = turning[i];
	train[1]++;
	return train;
}

function printer(image) {
	for (var y = 0; y < image.length; y++) {
		for (var x = 0; x < image[y].length; x++) {
			if (typeof image[y][x] == 'object')
				image[y][x] = image[y][x][0];
		}
		console.log(image[y].join(''))
	}
}

while (!crash) {
	console.log(iteration++);
	printer(input);
	for (var y = 0; y < input.length; y++) {
		for (var x = 0; x < input[y].length; x++) {
			train_check(x,y);
		}
	}
	if (iteration > 20)
		crash = true;
}