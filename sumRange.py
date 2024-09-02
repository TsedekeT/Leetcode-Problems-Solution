class NumArray:

   def __init__(self, nums: List[int]): # [-2, 0, 3, -5, 2, -1]
    self.prefixSum = []  #[-2, -2, 1, -4, -2, -3]
    currentSum = 0 
    
    for n in nums:
        currentSum += n 
        self.prefixSum.append(currentSum) 


    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefixSum[right]
        if left > 0:
            leftSum = self.prefixSum[left - 1]
        else:
            leftSum = 0
        return rightSum -leftSum
