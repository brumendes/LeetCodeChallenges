class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev = 0
        n = x
        if n < 0:
            return False
        while n > 0:
            rev = rev * 10 + n%10
            n = n//10    
        return rev == x

test = 121
sol = Solution()
print(sol.isPalindrome(test))