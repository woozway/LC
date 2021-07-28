// array, tree
// T=O(n)
// S=O(n)

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;

    Node() {}

    Node(int _val) {
        val = _val;
        left = NULL;
        right = NULL;
    }

    Node(int _val, Node* _left, Node* _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/
class Solution {
  vector<Node*> v;

public:
  Node* treeToDoublyList(Node* root) {
    if (root == nullptr) {
      return root;
    }
    dfs(root);
    for (int i = 0; i < v.size()-1; i++) {
      v[i]->right = v[i+1];
    }
    v[v.size()-1]->right = v[0];

    for (int i = v.size()-1; i > 0; i--) {
      v[i]->left = v[i-1];
    }
    v[0]->left = v[v.size()-1];
    return v[0];
  }

  void dfs(Node* node) {
    if (node == nullptr) {
      return;
    }
    dfs(node->left);
    v.push_back(node);
    dfs(node->right);
  }
};
