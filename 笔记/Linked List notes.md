# Linked List notes
---
## Two Pointer Technique
1. **leetcode 141. Linked List Cycle & leetcode 142. Linked List Cycle II**:
   - S=O(1) to detect cycle in a singly linked list, use fast & slow pointers
    ```java
    // Initialize slow & fast pointers
    ListNode slow = head;
    ListNode fast = head;
    /**
    * Change this condition to fit specific problem.
    * Attention: remember to avoid null-pointer error
    **/
    while (slow != null && fast != null && fast.next != null) {
      slow = slow.next;           // move slow pointer one step each time
      fast = fast.next.next;      // move fast pointer two steps each time
      if (slow == fast) {         // change this condition to fit specific problem
        return true;
      }
    }
    return false;   // change return value to fit specific problem
    ```
2. Tips:
   - Always examine if the node is null before you call the next field.
   - Carefully define the end conditions of your loop.
   - Going through some test cases will save you time.
   - Feel free to use several pointers at the same time.
   - In many cases, you need to track the previous node of the current node.
3. A comparison of time complexity between the linked list and the array:
   ![alt text](https://github.com/chopchap/leetcode/blob/main/images/comparison_of_time_complexity.png?raw=true)
