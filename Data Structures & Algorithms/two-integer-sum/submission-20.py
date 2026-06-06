class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {} # nums = [3,4,5,6], target = 7

        for i,num in enumerate(nums):
            diff = target-num
            if diff in numbers and numbers[diff] != i:
                return [min(i,numbers[diff]),max(i,numbers[diff])]
            numbers[num] = i
            
