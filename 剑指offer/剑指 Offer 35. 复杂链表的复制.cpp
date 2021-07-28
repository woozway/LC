// hashing, linkedlist
// T=O(n)
// S=O(n)

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/
class Solution {
public:
  Node* copyRandomList(Node* head) {
    if (head == nullptr) {
      return head;
    }
    vector<Node*> v;
    unordered_map<Node*, int> relativeIndex;
    Node* trav = head;
    int index = 0;
    while (trav) {
      v.push_back(new Node(trav->val));
      relativeIndex[trav] = index;
      trav = trav->next;
      index += 1;
    }
    for (int i = 0; i < v.size()-1; i++) {
      v[i]->next = v[i+1];
    }
    trav = head;
    index = 0;
    while (trav) {
      if (relativeIndex.find(trav->random) != relativeIndex.end()) {
        v[index]->random = v[relativeIndex[trav->random]];
      }
      trav = trav->next;
      index += 1;
    }
    return v[0];
  }
};
