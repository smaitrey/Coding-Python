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
