/*
Create a function that takes a number (step) as an argument and returns the number of matchsticks in that step. 
See step 1, 2 and 3 in the image above.
*/


function matchHouses(step) {
	return step === 0 ? 0 : 5 * step + 1;
}

console.log(matchHouses(1))