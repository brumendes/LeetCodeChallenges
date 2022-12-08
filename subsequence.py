class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        idx_t = 0
        idx_s = 0
        while idx_t < len(t) and idx_s < len(s):
            if t[idx_t] == s[idx_s]:
                idx_s += 1
            idx_t += 1
        return idx_s == len(s)


s = "ace"
t = "abcde"
sol = Solution()
print(sol.isSubsequence(s, t))