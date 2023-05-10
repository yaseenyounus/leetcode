class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for x in range(len(nums)):
            for y in range(1, len(nums)):
                if x == y:
                    continue
                elif nums[x] + nums[y] == target:
                    return [x, y]


s = Solution()
print(s.twoSum([1, 2, 5, 3, 5], 3))
print(s.twoSum([3, 2, 3], 6))
print(s.twoSum([2, 5, 5, 11], 10))
