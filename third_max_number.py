def thirMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums_set = list(set(nums))
    nums_set.sort()
    if len(nums_set) >= 3:
        ans = nums_set[-3]
    else:
        ans = max(nums_set)
    return ans


testCase = [-1,2,3]
print(thirMax(testCase))