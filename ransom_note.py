class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ans = None
        temp = []
        for r in ransomNote:
            if r in magazine:
                if r not in temp:
                    temp.append(r)
                    ans = True
                else:
                    if list(magazine).count(r) > temp.count(r):
                        temp.append(r)
                        ans = True
                    else:
                        ans = False
                        break
            else:
                ans = False
                break
        return ans


ransom_note = "fihjjjjei"
magazine = "hjibagacbhadfaefdjaeaebgi"

solution = Solution()
print(solution.canConstruct(ransom_note, magazine))