from numpy import result_type


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            char_map = []
            mapping = []
            result = []
            for idx, ch in enumerate(zip(s, t)):
                if ch[0] in char_map:
                    result.append(mapping[char_map.index(ch[0])])
                else:
                    if ch[1] in result:
                        return False
                    else:
                        char_map.append(ch[0])
                        mapping.append(ch[1])
                        result.append(ch[1])
        return result == list(t)
        # ans = True
        # map_char = dict(zip(s, t))
        # cleaned_map = {}
        # for key,value in map_char.items():
        #     if value not in cleaned_map.values():
        #         cleaned_map[key] = value
        # result = str()
        # for ch in s:
        #     if ch in cleaned_map:
        #         result += cleaned_map[ch]
        #     else:
        #         pass
        # if result == t:
        #     ans = True
        # else:
        #     ans = False
        # return ans


s = "aaaaabbbbbcccccdddddeeeee"
t = "pppppqqqqqrrrrrsssssttttt"
sol = Solution()
print(sol.isIsomorphic(s, t))