class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = None
        for i in range(0, len(nums) - 1):
            temp = nums[i + 1: len(nums)]
            for j, num in enumerate(temp):
                sum = nums[i] + num
                if sum == target:
                    ans = [i, i + j + 1]
                    break
        return ans


nums = [3,3]
target = 6
sol = Solution()
print(sol.twoSum(nums, target))