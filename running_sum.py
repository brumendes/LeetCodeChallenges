class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [nums[0]]
        for i in range(1, len(nums)):
            ans.append(ans[i - 1] + nums[i])
        return ans


test = [1,2,3,4]
sol = Solution()
print(sol.runningSum(test))