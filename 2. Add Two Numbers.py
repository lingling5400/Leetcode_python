# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        cur=dummy

        carry =0
        sums=0

        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            if v1!=None and v2!=None:
                a= v1 + v2+carry
                sums =( v1 + v2+carry)%10
                carry = a//10          #用/會出現浮點數，//會是正常的十位數(整數)
                cur.next=ListNode(sums)
                cur = cur.next
                
                if l1: l1 = l1.next
                if l2: l2 = l2.next

        if carry!=0:
            cur.next=ListNode(carry)
        return dummy.next




#優化版:把carry一起放進while裡少一個if
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            cur.next = ListNode(total % 10)
            cur = cur.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
