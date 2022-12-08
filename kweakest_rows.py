class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        ranks = []
        for i in range(0, len(mat)):
            n_soldiers = 0
            for j in range(0, len(mat[i])):
                if mat[i][j] == 1:
                    n_soldiers += 1
                else:
                    pass
            ranks.append((i, n_soldiers))
        ans = [x[0] for x in sorted(ranks, key=lambda x: x[1])][:k]
        return ans


mat = [[1,1,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,1,0,0,0],
    [1,1,1,1,1]]
k = 3
sol = Solution()
print(sol.kWeakestRows(mat, k))
    
