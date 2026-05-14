# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = node = ListNode(0, head)
        while node:
            kth = self.getKth(node, k)
            if not kth:
                break
            kthNext = kth.next
            
            curNode = node.next
            prev = kth.next
            while curNode != kthNext:
                tmp = curNode.next
                curNode.next = prev
                prev = curNode
                curNode = tmp
            
            tmp = node.next
            node.next = kth
            node = tmp
        
        return dummy.next



    
    def getKth(self, cur, k):
        while cur and k:
            cur = cur.next
            k -= 1
        return cur