//   Write a function that takes in a non-empty array of integers that are sorted
//   in ascending order and returns a new array of the same length with the squares
//   of the original integers also sorted in ascending order.

let array = [-50, 1, 2, -3, 5, -6, 7, 8, 9]
// let array = [-5, -4, -3, -2, -1]
//  25, 16 , 9, 4 , 1
console.log(array.length, 'length');


function sortedSquaredArray(array) {
    // Write your code here.
    let squared = []
    let holder;
    for (let i = 0; i < array.length; i++) {
        squared.push(array[i] * array[i])
        for(let runner = 0; runner < squared.length; runner++){
            // console.log(runner,i, squared);
            // because all int in array are unique we can do this
            if(squared[runner] !==squared[i]){
                if(squared[runner] > squared[i]){
                    holder = squared[i]
                    squared[i] = squared[runner]
                    squared[runner] = holder
                }
            }
        }
    }
    console.log(squared)
    return squared;
}


sortedSquaredArray(array)