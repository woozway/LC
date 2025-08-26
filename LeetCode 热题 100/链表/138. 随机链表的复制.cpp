class Solution {
  unordered_map<Node *, Node *> M;

public:
  Node* copyRandomList(Node* head) {
    // for (Node *t = head; t; t = t->next->next)
    //   t->next = new Node(t->val, t->next, nullptr);
    
    // for (Node *t = head; t; t = t->next->next)
    //   if (t->random) t->next->random = t->random->next;
    
    // Node *p = head->next;
    // Node *t = head;
    // for ( ; t->next->next; t = t->next) {
    //   Node *copy = t->next;
    //   t->next = copy->next;
    //   copy->next = copy->next->next;
    // }
    // t->next = nullptr;
    // return p;

    // 递归解
    if (!head) return nullptr;

    if (!M.count(head)) {
      Node *p = new Node(head->val);
      M[head] = p;
      p->next = copyRandomList(head->next);
      p->random = copyRandomList(head->random);
    }
    return M[head];
  }
};