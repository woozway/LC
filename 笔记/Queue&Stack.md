# Queue & Stack
---
## notes:
- **leetcode 133. Clone Graph**
   > deep copy is the essence of Garbage Collection mechanism, remember to clone node first then dive into recursion, otherwise it might loop inside a graph. (since the depth of human thinking is quite limited, when implementing dfs, we need only focusing on one level of implementation and remember the outcome that you want you dfs to have, then leave the rest of things to system stack, it'll take care of that)
- **leetcode 394. Decode String**
  1. technique to first store previous string in stack
  2. master the resursive solution (note: don't forget to `pre_num = 0` since when you've done one [...]'s handling)
## bfs
```java
// BFS_template I
/**
 * Return the length of the shortest path between root and target node.
 */
int BFS(Node root, Node target) {
  Queue<Node> queue;  // store all nodes which are waiting to be processed
  int step = 0;       // number of steps neeeded from root to current node
  // initialize
  add root to queue;
  // BFS
  while (queue is not empty) {
    step = step + 1;
    // iterate the nodes which are already in the queue
    int size = queue.size();
    for (int i = 0; i < size; ++i) {
      Node cur = the first node in queue;
      return step if cur is target;
      for (Node next : the neighbors of cur) {
        add next to queue;
      }
      remove the first node from queue;
    }
  }
  return -1;          // there is no path from root to target
}


// BFS_template II
/**
 * Return the length of the shortest path between root and target node.
 */
int BFS(Node root, Node target) {
  Queue<Node> queue;  // store all nodes which are waiting to be processed
  Set<Node> visited;  // store all the nodes that we've placed in Queue
  int step = 0;       // number of steps neeeded from root to current node
  // initialize
  add root to queue;
  add root to visited;
  // BFS
  while (queue is not empty) {
    step = step + 1;
    // iterate the nodes which are already in the queue
    int size = queue.size();
    for (int i = 0; i < size; ++i) {
      Node cur = the first node in queue;
      return step if cur is target;
      for (Node next : the neighbors of cur) {
        if (next is not in used) {
          add next to queue;
          add next to visited;
        }
      }
      remove the first node from queue;
    }
  }
  return -1;          // there is no path from root to target
}


// There are some cases where one does not need keep the visited hash set:

// 1. You are absolutely sure there is no cycle, for example, in tree traversal;
// 2. You do want to add the node to the queue multiple times.
```
## dfs
```java
/*
 * Return true if there is a path from cur to target.
 */
boolean DFS(Node cur, Node target, Set<Node> visited) {
  return true if cur is target;
  for (next : each neighbor of cur) {
    if (next is not in visited) {
      add next to visted;
      return true if DFS(next, target, visited) == true;
    }
  }
  return false;
}


/*
 * Return true if there is a path from cur to target.
 */
boolean DFS(int root, int target) {
  Set<Node> visited;
  Stack<Node> stack;
  add root to stack;
  while (s is not empty) {
    Node cur = the top element in stack;
    remove the cur from the stack;
    return true if cur is target;
    for (Node next : the neighbors of cur) {
      if (next is not in visited) {
        add next to visited;
        add next to stack;
      }
    }
  }
  return false;
}


// the first path you found in DFS might not be the shortest path.
// What if you want to find the shortest path? Add one more 
// parameter to indicate the shortest path you have already found.

// the size of the stack is exactly the depth of DFS. So in the 
// worst case, it costs O(h) to maintain the system stack, 
// where h is the maximum depth of DFS.
```
