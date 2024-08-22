class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize the pointer k
        k = 0
        
        # Iterate over each element in the nums array
        for i in range(len(nums)):
            # If the current element is not equal to val
            if nums[i] != val:
                # Place it at the k-th position and increment k
                nums[k] = nums[i]
                k += 1
        
        # Return the number of elements not equal to val
        return k
