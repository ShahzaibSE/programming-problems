# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# from typing import Optional

# def addTwoNumbers(l1, l2):
#     sums = []
#     if(l1.next != None and l2.next != None):
#         print('There are elements')
#     for i in range(len(l1)):
#         tempSum = l1[i] + l2[i]
#         tempSum_str = str(tempSum)
#         if(len(tempSum_str) == 2):
#             print("Two digits")
#         # if(tempSum_str[0])
#         # for j in range(i, len(l2)):
#         sums.append(tempSum)
#     return sums

# print(addTwoNumbers([2,4,3], [5,6,4]))

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], c = 0) -> Optional[ListNode]:
        val = l1.val + l2.val + c 
        c = val // 10
        ret = ListNode(val % 10)
        #
        if(l1.next != None or l2.next != None or c != 0):
            if(l1.next == None):
                l1.next = ListNode(0)
            if(l2.next == None):
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next, l2.next, c)
        return ret
