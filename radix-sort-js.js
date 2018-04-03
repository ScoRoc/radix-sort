
let radixSort = arr => {
  // if array is empty or 1 number
  if (arr.length === 0 || arr.length === 1) {
    return arr;
  }

  // define number of buckets
  let bucketCount = 10;
  let buckets = [];
  for (let i = 0; i < 10; i++) {
    buckets.push([]);
  }

  // converting each number in array to a string
  // and finding length of string(number) to find max_digits
  let max_digits = 0;
  arr.forEach(n => {
    if (n.toString().length > max_digits) {
      max_digits = n.toString().length;
    }
  });

  // new sorted array
  let sorted_arr = arr;

  // determines which digit to sort by
  let which_digit = 1;

  // loops thru for each digit thru max_digits
  for (let i = 0; i < max_digits; i++) {
    // loops thru each num in arr
    for (let j = 0; j < sorted_arr.length; j++) {
      // adds num at current digit to appropriate bucket
      buckets[ Math.floor( sorted_arr[j] / which_digit ) % 10].push(sorted_arr[j]);
    }
    console.log('~~~~Buckets at', i + 1, 'digit:', buckets);
    console.log('');
    // increments to next digit
    which_digit = which_digit * 10;
    // clears sorted_arr so it receives a clean push
    sorted_arr = [];
    // pushes sorted order for current digit into sorted_arr
    for (let b = 0; b < buckets.length; b++) {
      sorted_arr = [...sorted_arr, ...buckets[b] ];
      // clears buckets for next sort
      buckets[b] = [];
    }
  }

  console.log(sorted_arr);

};

let my_arr = [74, 2545, 21, 306, 42, 879, 33, 562, 4078, 93, 1395, 461, 50, 747, 124, 8359, 84, 6487, 246, 648, 2070];
radixSort(my_arr);
