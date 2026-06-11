class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1,2,4,6]
        # output = [48,24,12,8]
        n = len(nums)
        pref = [0] * n
        suff = [0] * n
        res = [0] * n
        pref[0] = 1
        suff[n-1] = 1

        for i in range(1,n):
            pref[i] = nums[i-1]*pref[i-1]
        for i in range(n-2,-1,-1):
            suff[i] = nums[i+1]*suff[i+1]
        # now the pref = [1,2,8,48], suff = [48,48,24,6]
        for i in range(i,n):
            res[i] = pref[i] * suff[i]
        return res

