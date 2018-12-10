const fs = require('fs');

var raw_input = fs.readFileSync('input/10.txt','utf8').trim();

var input = raw_input.split("\n").map(function(i) {
	return i.match(/[\-0-9]+/g).map(function(i) {
		return parseInt(i);
	});;
});

// 1001 & 1002 -------------------------------------------

var seconds = 0;
var area = null;

while (true) {
	seconds++;
	var x_min = Math.min.apply(Math, input.map(function(x) {return x[0]+x[2]*seconds}));
	var x_max = Math.max.apply(Math, input.map(function(x) {return x[0]+x[2]*seconds}));
	var y_min = Math.min.apply(Math, input.map(function(y) {return y[1]+y[3]*seconds}));
	var y_max = Math.max.apply(Math, input.map(function(y) {return y[1]+y[3]*seconds}));

	var new_area = (x_max-x_min)*(y_max-y_min);

	if (new_area < area || area == null)
		area = new_area;
	else {
		var render_array = new Array(y_max-y_min+1).fill('.');
		for (y in render_array) {
			render_array[y] = new Array(x_max-x_min+1).fill('.');
		}
		for (i of input) {
			var x = i[0]+i[2]*(seconds-1)-x_min;
			var y = i[1]+i[3]*(seconds-1)-y_min;
			render_array[y][x] = '#';
		}
		console.log('1001:');
		for (y of render_array) {
			console.log(y.join(''));
		}
		console.log('1002:',seconds-1);
		break;
	}
}