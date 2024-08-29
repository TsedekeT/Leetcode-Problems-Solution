class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                max_num = max(max_num,count)
            else:
                count = 0
        return max_num
