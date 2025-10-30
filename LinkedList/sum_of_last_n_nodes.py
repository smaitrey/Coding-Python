# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def sumOfLastN_Nodes(self, head, n):
        #function should return sum of last n nodes
        stack = []
        ans = 0
        while head:
            stack.append(head.data)
            head = head.next
            
        while n > 0 and stack:
            ans += stack.pop()
            n -= 1
            
        return ans

## M2: Using the length of linked list
def sumOfLastN_Nodes(self, head, n):
        #function should return sum of last n nodes
        ans = 0
        length = 0
        temp = head
        
        while temp:
            length += 1
            temp = temp.next
            
        count = length - n
        temp = head
        
        while temp and count > 0:
            temp = temp.next
            count -= 1
            
        while temp:
            ans += temp.data
            temp = temp.next
            
        return ans


