class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeros = 0
        for num in nums:
            if num:
                prod *= num
            else:
                zeros += 1
        if zeros > 1:
            return [0] * len(nums)

        res = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] != 0 and zeros:
                res[i] = 0
            elif nums[i] != 0 and not zeros:
                res[i] = prod//nums[i]
            else:
                res[i] = prod
        return res