class Solution {
public:
  ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
    // 两个链表都走完，不相交返回null
    auto a = headA, b = headB;
    while (a != b) {
      if (a) a = a->next;
      else a = headB;
      if (b) b = b->next;
      else b = headA;
    }
    return a; // 或b
  }
};