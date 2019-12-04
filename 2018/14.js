const fs = require('fs');

var input = parseInt(fs.readFileSync('input/14.txt','utf8').trim());

// 1401 --------------------------------------------------

var recipes = [3,7];

var elfs = [0,1];

while (recipes.length < input+10) {
	var sum = recipes[elfs[0]] + recipes[elfs[1]];
	if (sum > 9)
		recipes.push(1);
	recipes.push(sum%10);
	elfs[0] = (elfs[0] + recipes[elfs[0]] + 1) % recipes.length;
	elfs[1] = (elfs[1] + recipes[elfs[1]] + 1) % recipes.length;
}

console.log('1401:',recipes.join('').substr(recipes.length-10));

// 1402 --------------------------------------------------

recipes = [3,7];

elfs = [0,1];
var len = (''+input).length;
var last = '#'.repeat((''+input).length);

var i = 0;

while (true) {
	var sum = recipes[elfs[0]] + recipes[elfs[1]];
	if (sum > 9) {
		recipes.push(1);
		last += 1;
	}
	last = last.substr(last.length-len);
	if (last == input)
		break;
	recipes.push(sum%10);
	last += sum%10;
	last = last.substr(last.length-len);
	elfs[0] = (elfs[0] + recipes[elfs[0]] + 1) % recipes.length;
	elfs[1] = (elfs[1] + recipes[elfs[1]] + 1) % recipes.length;
	if (last == input)
		break;
}

console.log('1402:',recipes.length-len);