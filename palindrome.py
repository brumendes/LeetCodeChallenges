# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
  def __init__(self):  
    self.head = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        return head


test_case = [1,2,2,1]
LL = LinkedList()
LL.head = ListNode(test_case)
print(LL.head.val)
#solution = Solution()
#print(solution.isPalindrome(linked_list))