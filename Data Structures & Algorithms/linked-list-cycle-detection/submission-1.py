# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited ={
            # node : (visited_bool, index)
        }
        flag=False
        curr = head
        c=0
        while curr!=None and flag==False:
            if curr in visited:
                flag = True
                return True
            else:
                visited[curr] = (True, c)
                c=c+1
            curr = curr.next
        return False
