class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = -1 
        left_sum = 0
        right_sum = sum(nums)
        for i in range(0, len(nums)):
            right_sum -= nums[i]
            if left_sum == right_sum:
                ans = i
                break
            left_sum += nums[i]
        return ans


nums = [-1,-1,0,0,-1,-1]
sol = Solution()
print(sol.pivotIndex(nums))