class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        totalSum = sum(nums)
        for indx in range(len(nums)):
            if leftSum == totalSum -leftSum - nums[indx]:
                return indx
            
            leftSum += nums[indx]
        return -1       
