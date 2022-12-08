class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        wealth_list = []
        ans = None
        for client in accounts:
            wealth_list.append(sum(client))
        ans = max(wealth_list)
        return ans


accounts = [[1,5],[7,3],[3,5]]
sol = Solution()
print(sol.maximumWealth(accounts))