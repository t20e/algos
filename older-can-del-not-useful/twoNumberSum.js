// let array = [3, 5, -4, 8, 11, 1, -1, 6]
// let targetSum = 10;
// test case 2
// let array = [3, 5, -4, 8, 11, 1, -1, 6]
// let targetSum = 15;
// test case 3
let array = [6, -4, 5,3,92,-8,12,8,-5,2,89,12,98,63,98,55,4,-78,17]
let targetSum = 25;

function twoNumberSum(array, targetSum) {
    // Write your code here.
    for (let startNum = 0; startNum < array.length; startNum++) {
        for (let runner = 0; runner < array.length; runner++) {
            if (runner == startNum) {
                // console.log('continue', runner ,startNum);
                continue;
            }
            if (array[startNum] + array[runner] == targetSum) {
                return [array[runner], array[startNum]];
            }
        }
    }
    return [];
}
console.log(twoNumberSum(array, targetSum));

// other solution

// function twoNumberSum(array, targetSum) {
//     // Write your code here.
//     const findSum = (start) => {
//         for (let runner = 0; runner < array.length; runner++) {
//             // skip the current i if the i and start is at the same spot]!!
//             console.log('here');
//             if (start > array.length -1) {
//                 console.log('no numbers equal target sum')
//                 return false;
//             }
//             if (start === runner) {
//                 continue;
//             } else if (array[start] + array[runner] == targetSum) {
//                 console.log(array[runner], array[start]);
//                 return 'found sum';
//             } else if (runner == array.length - 1) {
//                 // console.log('looping');
//                 start++;
//                 findSum(start);
//             }
//             console.log(start);
//         }
//     }
//     findSum(0);
// }
// twoNumberSum(array, targetSum);