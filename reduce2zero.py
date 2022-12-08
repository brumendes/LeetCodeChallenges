class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        num_temp = num
        while num_temp >= 0:
            if num_temp == 0:
                break
            else:
                if (num_temp % 2) == 0:
                    num_temp = num_temp/2
                else: 
                    num_temp = num_temp - 1
                steps += 1
        return steps    

num = 0
sol = Solution()
print(sol.numberOfSteps(num))