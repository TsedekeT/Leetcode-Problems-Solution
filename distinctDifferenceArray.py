class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_set = set()
        suffix_set = set(nums)
        suffix_count = {}
        diff = []
        for num in nums:
            suffix_count[num] = suffix_count.get(num, 0) + 1

        for i in range(n):
            prefix_set.add(nums[i])
            suffix_count[nums[i]] -= 1
            if suffix_count[nums[i]] == 0:
                suffix_set.discard(nums[i])
            diff.append(len(prefix_set) - len(suffix_set))
        
        return diff

