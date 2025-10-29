""""
Given a singly linked list. The task is to find the sum of nodes of the given linked list.
Input: 7->6->8->4->1
Output: 26

Definition of Node 
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

""""

def get_sum(head):
  ans = 0
  curr = head
  while curr:
    ans += head.val
    curr = curr.next

  return ans


def get_sumr(head):
  if not head:
    return 0

  return head.val + get_sumr(head.next)
  
