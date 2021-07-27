// stack
// T=O(n)
// S=O(n)

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
  vector<int> reversePrint(ListNode* head) {
    stack<int> s;
    ListNode *trav = head;
    while (trav) {
      s.push(trav->val);
      trav = trav->next;
    }
    vector<int> v;
    while (!s.empty()) {
      v.push_back(s.top());
      s.pop();
    }
    return v;
  }
};
