def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    roman2int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    if 1 <= len(s) <= 15:
        ans = 0
        idx = 0
        length = len(s)
        while idx < length:
            if s[idx] in roman2int:
                s_curr = s[idx]
                if idx == len(s) - 1:
                    value = roman2int.get(s_curr)
                    ans += value
                    break
                else: 
                    s_next = s[idx + 1]
                    if s_curr == 'I' and (s_next == 'V' or s_next == 'X'):    
                        value = roman2int.get(s_next) - roman2int.get(s_curr)
                        idx += 2
                    elif s_curr == 'X' and (s_next == 'L' or s_next == 'C'):
                        value = roman2int.get(s_next) - roman2int.get(s_curr)
                        idx += 2
                    elif s_curr == 'C' and (s_next == 'D' or s_next == 'M'):
                        value = roman2int.get(s_next) - roman2int.get(s_curr)
                        idx += 2
                    else:
                        value = roman2int.get(s_curr)
                        idx += 1
                ans += value
            else:
                print("Input must be one of the following: %r." % list(roman2int.keys()))
                break
    else:
        print('Roman number has more than 15 characters.')
    return ans


test_case = 'MCMXCIV'
print(romanToInt(test_case))