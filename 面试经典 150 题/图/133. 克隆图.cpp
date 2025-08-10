class Solution {
  unordered_map<Node *, Node *> st;

public:
  Node* cloneGraph(Node* node) {
    if (!node) return nullptr;

    if (st.count(node)) return st[node];

    Node *c = new Node(node->val);
    st[node] = c;

    for (auto &x : node->neighbors) c->neighbors.push_back(cloneGraph(x));
    return c;
  }
};