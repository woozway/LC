class Solution:
  def isPalindrome(self, head: ListNode) -> bool:
    v = []
    while head:
      v.append(head.val)
      head = head.next
    i = 0
    j = len(v)-1
    while i < j:
      if v[i] != v[j]:
        return False
      i += 1
      j -= 1
    return True
