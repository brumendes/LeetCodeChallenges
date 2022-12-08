from sys import prefix


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = []
        counts = 0
        for i in range(0, len(strs) - 1):
            for j in strs[i]:
                if j in strs[i + 1]:
                    ans.append(j)
        for l in range(0, len(ans)):
            if l in ans:
                counts += 1
        return counts


strs = ["flower","flow","flight"]
sol = Solution()
print(sol.longestCommonPrefix(strs))