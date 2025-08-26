class Solution {
public:
  ListNode *detectCycle(ListNode *head) {
    // slow走了b步和fast相遇于环中某一节点，则 b*2 - b = k*c，c为环长，k为整数 => b = k*c
    // 设a为head到入环口长度，则 b - a = k*c - a，此时让slow和head一起走，再走a步二者相遇于环口
    ListNode *slow = head, *fast = head;
    while (fast && fast->next) {
      slow = slow->next, fast = fast->next->next;
      if (fast == slow) {
        while (slow != head)
          slow = slow->next, head = head->next;
        return slow;
      }
    }
    return nullptr;
  }
};