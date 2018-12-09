const fs = require('fs');

var raw_input = fs.readFileSync('input/09.txt','utf8').trim();

var input = raw_input.split(' ');

// 0901 & 0902 -------------------------------------------

var players = parseInt(input[0]);
var marbles = parseInt(input[6]);

var start = process.hrtime();

function game(players,marbles) {
	var scores = new Array(players).fill(0);

	var current_marble = {"value": 0, "next":null, "prev":null};
	current_marble.prev = current_marble;
	current_marble.next = current_marble;

	for (var m = 1; m <= marbles; m++) {
		if (m % 23 == 0) {
			scores[m % players] += m;
			for (i = 0; i < 7; i++) current_marble = current_marble.prev;
			scores[m % players] += current_marble.value;
			current_marble.prev.next = current_marble.next;
			current_marble.next.prev = current_marble.prev;
			current_marble = current_marble.prev.next;
		} else {
			var new_marble = {"value": m, "next": current_marble.next.next, "prev": current_marble.next};
			current_marble.next.next.prev = new_marble;
			current_marble.next.next = new_marble;
			current_marble = new_marble;
		}
	}

	return Math.max(...scores);
}

console.log('0901:',game(players,marbles));

console.log('0902:',game(players,marbles*100));