class Solution {
public:
  bool hasCycle(ListNode *head) {
    // 如果有环，快慢指针终会相遇
    ListNode *slow = head, *fast = head;
    while (fast && fast->next) {
      slow = slow->next, fast = fast->next->next;
      if (fast == slow) return true;
    }
    return false;
  }
};