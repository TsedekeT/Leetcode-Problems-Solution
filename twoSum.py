class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        result = []

        while start < end:
            sum = numbers[start] + numbers[end]
            if sum == target:
                result.append(start + 1)
                result.append(end + 1)
                return result
            elif sum > target:
                end -= 1
            else:
                 start += 1
