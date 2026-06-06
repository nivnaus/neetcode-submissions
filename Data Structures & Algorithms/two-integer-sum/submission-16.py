class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i,num in enumerate(nums):
            numbers[num] = i # val, index

        for i,num in enumerate(nums):
            diff = target-num
            if diff in numbers and numbers[diff] != i:
                return [min(numbers[diff],i),max(numbers[diff],i)]
            
        return []
        
