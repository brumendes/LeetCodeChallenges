def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cnt = 0
    ans = 0
    diff = None
    for idx in range(1, len(nums)):
        newdiff = nums[idx] - nums[idx - 1]
        if newdiff == diff:
            ans += cnt
            cnt +=1
        else:
            diff = newdiff
            cnt = 1
    return ans

test_case = [1,2,3,4,5,6]
print(numberOfArithmeticSlices(test_case))