// Write a function:

// function solution(A);

// that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

// For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

// Given A = [1, 2, 3], the function should return 4.

// Given A = [−1, −3], the function should return 1.

// Write an efficient algorithm for the following assumptions:

// N is an integer within the range [1..100,000];
// each element of array A is an integer within the range [−1,000,000..1,000,000].
// Copyright 2009–2021 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

let num_list = [1, 3, 6, 4, 1, 2]

function findSmallestPositiveInteger(values){
    // for(let i=0; i<nums.length;i++){
    //     if(num[i] < 1000000 && num[i] > 1000000) {
    //         break;
    //     }else {

    //     }
    // }
    let result = [];

    for (let i = 0; i < values.length; ++i) {
        if (0 <= values[i]) {
            result[values[i]] = true;
        }
    }

    for (let i = 1; i <= result.length; ++i) {
        if (undefined === result[i]) {
            return i;
        }
    }

    return 1
}

console.log(findSmallestPositiveInteger(num_list))