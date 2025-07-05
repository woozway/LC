class Solution {
  ListNode* middleNode(ListNode* head) {
    ListNode *slow = head, *fast = head;
    while (fast && fast->next)
      slow = slow->next, fast = fast->next->next;
    return slow;
  }

  ListNode* reverseList(ListNode* head) {
    ListNode *pre = nullptr, *cur = head;
    while (cur) {
      ListNode *nxt = cur->next;
      cur->next = pre, pre = cur, cur = nxt;
    }
    return pre;
  }
  
public:
  bool isPalindrome(ListNode* head) {
    auto &a = head;
    ListNode *mid = middleNode(a);
    ListNode *b = reverseList(mid);
    while (b) {
      if (a->val != b->val) return false;
      a = a->next, b = b->next;
    }
    return true;
  }
};