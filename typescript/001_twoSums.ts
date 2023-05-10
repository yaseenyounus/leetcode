function twoSum(nums: number[], target: number): number[] {
  for (let x = 0; x < nums.length; x++) {
    for (let y = 1; y < nums.length; y++) {
      if (x === y) {
        continue;
      } else if (nums[x] + nums[y] === target) {
        return [x, y];
      }
    }
  }
  return [];
}

console.log(twoSum([1, 2, 5, 3, 5], 3));
console.log(twoSum([3, 2, 3], 6));
console.log(twoSum([2, 5, 5, 11], 10));
