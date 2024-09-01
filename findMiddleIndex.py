class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftSum = 0
        totalSum = sum(nums)
        for middleIndex in range(len(nums)):
            if leftSum == totalSum - leftSum - nums[middleIndex]:
                return middleIndex
            leftSum += nums[middleIndex]
        return -1
