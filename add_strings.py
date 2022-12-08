def addStrings(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    num_zeros = None
    ans = []
    ans1 = str()
    carry = 0
    if len(num1) < len(num2):
        num_zeros = len(num2) - len(num1)
        for t in range(0, num_zeros):
            num1 = "0" + num1
    else:
        num_zeros = len(num1) - len(num2)
        for t in range(0, num_zeros):
            num2 = "0" + num2
    for idx, num in enumerate(num2[::-1]):
        rslt = str(int(num1[idx]) + int(num2[idx]) + carry)
        if len(rslt) > 1:
            carry = int(rslt[0])
            ans1 = ans1 + (str(rslt))
        else:
            carry = 0
            ans1 = ans1 + (str(rslt))
    return ans1


num1 = "456"
num2 = "77"

print(addStrings(num1, num2))