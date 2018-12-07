const fs = require('fs');

var raw_input = fs.readFileSync('input/07.txt','utf8').trim();

var input = raw_input.split("\n");

function construct(delay, elfs) {
	var deps = {};

	var order = "";

	var workers = new Array(elfs).fill('.');

	var l = 0;

	for (w in workers)
		workers[w] = {'ready': null, 'step': null};

	for (var i = 'A'.charCodeAt(0); i <= 'Z'.charCodeAt(0); i++) {
		deps[String.fromCharCode(i)] = [];
		l++;
	}

	for (i of input) {
		var split = i.split(' ');
		deps[split[7]].push(split[1]);
	}

	var time = -1;

	while (order.length < l) {
		for (w in workers){
			if (workers[w]['ready'] == time) {
				order += workers[w]['step'];
				for (r in deps) {
					if (deps[r].indexOf(workers[w]['step']) > -1) {
						deps[r].splice(deps[r].indexOf(workers[w]['step']),1);
					}
				}
				workers[w]['ready'] = null;
				workers[w]['step'] = null;
			}
			if (workers[w]['ready'] == null) {
				for (d in deps) {
					if (deps[d].length == 0) {
						delete deps[d];
						if (elfs == 1)
							workers[w]['ready'] = time+1;
						else
							workers[w]['ready'] = time + delay + d.charCodeAt(0)-64;
						workers[w]['step'] = d;
						break;
					}
				}
			}
		}
		time++;
	}
	return [order,time-1];
}

// 0701 --------------------------------------------------

console.log('0701:',construct(0,1)[0]);

// 0701 --------------------------------------------------

console.log('0702:',construct(60,5)[1]);