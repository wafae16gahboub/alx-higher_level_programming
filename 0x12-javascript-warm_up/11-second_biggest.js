#!/usr/bin/node

function findSecondBiggest(numbers) {
  if (numbers.length <= 1) {
    return 0;
  }

  let [biggest, secondBiggest] = [-Infinity, -Infinity];

  for (let i = 0; i < numbers.length; i++) {
    const currentNumber = parseInt(numbers[i], 10);

    if (currentNumber > biggest) {
      secondBiggest = biggest;
      biggest = currentNumber;
    } else if (currentNumber > secondBiggest && currentNumber < biggest) {
      secondBiggest = currentNumber;
    }
  }

  return secondBiggest;
}

const args = process.argv.slice(2);
console.log(findSecondBiggest(args));
