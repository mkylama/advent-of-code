const fs = require('fs');

var raw_input = fs.readFileSync('input/08.txt','utf8').trim();

var input = raw_input.split(' ').map(function(i) {
	return parseInt(i);
});

// 0801 --------------------------------------------------

var i = 0;

function node(start) {
	var child_nodes = input[i++];
	var meta_count = input[i++];
	var meta_total = 0;
	for (var c = 0; c < child_nodes; c++)
		meta_total += node(i);
	for (var m = 0; m < meta_count; m++)
		meta_total += input[i++];
	return meta_total;
}

console.log('0801:',node(i));

var i = 0;

function root(start) {
	var child_nodes = input[i++];
	var meta_count = input[i++];
	var child_total = [0];
	var meta_total = 0;
	for (var c = 0; c < child_nodes; c++)
		child_total[c+1] = root(i);
	for (var m = 0; m < meta_count; m++) {
		if (child_nodes == 0) {
			meta_total += input[i++];
		} else {
			if (child_total[input[i]] != undefined)
				meta_total += child_total[input[i]];
			i++;
		}

	}
	return meta_total;
}

console.log('0802:',root(i));