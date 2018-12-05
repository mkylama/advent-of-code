const fs = require('fs');

var input = fs.readFileSync('input/05.txt','utf8').trim();

// 0501 --------------------------------------------------

function react(comp) {
	var i = 0;

	while (i < comp.length - 1) {
		if (Math.abs(comp.charCodeAt(i) - comp.charCodeAt(i + 1)) == 32) {
			comp = comp.substr(0,i) + comp.substr(i + 2);
			if (i > 0) i--;
		} else {
			i++;
		}
	}

	return comp;
}

console.log('0501:',react(input).length);

// 0502 --------------------------------------------------

var units = [];

for (var unit = 'A'.charCodeAt(0); unit <= 'Z'.charCodeAt(0); unit++) {
	units.push(react(input.replace(new RegExp(String.fromCharCode(unit),'gi'),'')).length);
}

console.log('0502:',Math.min(...units));