const fs = require('fs');

var raw_input = fs.readFileSync('input/23.txt','utf8').trim();

araw_input = `set a 5
sub a 3`;

var input = raw_input.split("\n");

// 0501 --------------------------------------------------

var regs = {
	'a': 0,
	'b': 0,
	'c': 0,
	'd': 0,
	'e': 0,
	'f': 0,
	'g': 0,
	'h': 0
}

var i = 0;
var c = 0;
var mul = 0;

while (i < input.length) {
	var s = input[i].split(' ');
	if (s[0] == 'set') {
		if (s[2] in regs)
			regs[s[1]] = regs[s[2]]
		else
			regs[s[1]] = parseInt(s[2])
	} else if (s[0] == 'sub') {
		if (s[2] in regs)
			regs[s[1]] -= regs[s[2]]
		else
			regs[s[1]] -= parseInt(s[2])
	} else if (s[0] == 'mul') {
		mul++;
		if (s[2] in regs)
			regs[s[1]] *= regs[s[2]]
		else
			regs[s[1]] *= parseInt(s[2])
	} else if (s[0] == 'jnz') {
		if (s[1] in regs)
			x = regs[s[1]]
		else
			x = parseInt(s[1])
		if (s[2] in regs)
			y = regs[s[2]]
		else
			y = parseInt(s[2])
		if (x != 0)
			i += y - 1;
	} 
	console.log(i)
	i++;
}

console.log(regs);
console.log(mul);