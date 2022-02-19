# Tree
---
## Binary Tree
### solve Tree Problems Recursively
- "Top-down" Solution:
  - "top-down" means that in each recursive call, we will visit the node first to come up with some values, and pass these values to its children when calling the function recursively. So the "top-down" solution can be considered as a kind of preorder traversal.
    ```java
    1. return specific value for null node
    2. update the answer if needed                      // answer <-- params
    3. left_ans = top_down(root.left, left_params)      // left_params <-- root.val, params
    4. right_ans = top_down(root.right, right_params)   // right_params <-- root.val, params
    5. return the answer if needed                      // answer <-- left_ans, right_ans
    ```
- "Bottom-up" Solution:
  - in each recursive call, we will firstly call the function recursively for all the children nodes and then come up with the answer according to the returned values and the value of the current node itself. This process can be regarded as a kind of postorder traversal.
    ```java
    1. return specific value for null node
    2. left_ans = bottom_up(root.left)      // call function recursively for left child
    3. right_ans = bottom_up(root.right)    // call function recursively for right child
    4. return answers                       // answer <-- left_ans, right_ans, root.val
    ```
- Conclusion
  - When you meet a tree problem, ask yourself two questions:
    - Can you determine some parameters to help the node know its answer?
    - Can you use these parameters and the value of the node itself to determine what should be the parameters passed to its children?
  - If the answers are both yes, try to solve this problem using a "top-down" recursive solution.
  - Or, you can think of the problem in this way:
    - for a node in a tree, if you know the answer of its children, can you calculate the answer of that node?
  - If the answer is yes, solving the problem recursively using a bottom up approach might be a good idea.
## N-ary Tree
### traversal
- Note that here is no standard definition for in-order traversal in n-ary trees. It probably only makes sense for binary trees.
- Note that the reversed order of preorder traversal sequence of n-ary tree (from right to left) is the postorder traversal of itself.
- "Top-down" Solution:
    ```java
    1. return specific value for null node
    2. update the answer if needed                              // answer <-- params
    3. for each child node root.children[k]:
    4.      ans[k] = top_down(root.children[k], new_params[k])  // new_params <-- root.val, params
    5. return the answer if needed                              // answer <-- all ans[k]
    ```
- "Bottom-up" Solution:
    ```java
    1. return specific value for null node
    2. for each child node root.children[k]:
    3.      ans[k] = bottom_up(root.children[k])    // call function recursively for all children
    4. return answer                                // answer <- root.val, all ans[k]
    ```
