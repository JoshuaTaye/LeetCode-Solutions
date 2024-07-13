class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l = listNode()
        i,j = 0,0
        itr1 = l1.head
        while itr1.next:
            itr1 = itr1.next
        itr2 = l2.head
        while itr2.next:
            itr2 = itr2.next        
        while i < itr1 and j < itr2:
            if l1[i] <= l2[j]:
                l.append(l1[i])
                i += 1
            else:
                l.append(l2[j])
                j += 1
        if j < len(l2):
            while j < len(l2):
                l.append(l2[j])
                j += 1
        elif i < len(l1):
            while i < len(l1):
                l.append(l1[i])
                i += 1    
        return l   

lst1 = input().strip('[').strip(']').split(',')
lst2 = input().strip('[').strip(']').split(',')
merge(lst1, lst2)