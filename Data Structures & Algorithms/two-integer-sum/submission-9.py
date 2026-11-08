class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            bel = target - num

            if bel in nums[i + 1:]:
                return [i, nums.index(bel, i + 1)]










#for i in nums:
            #bel = target - i
            #if (bel in nums) and nums.index(i, )!=nums.index(bel):
             #   return [nums.index(i), nums.index(bel)]    
            #bel = target    
