class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            bel = target - num

            if bel in nums[i + 1:]:
                return [i, nums.index(bel, i + 1)]











