# Hash Table
---
## usage of collections.xxx() in py3
- leetcode 350. Intersection of Two Arrays II
- Counter().keys() != Counter.elements(), the latter shows each appearance of an element in Counter
- Counters can be &'d
- defaultdict(list) can initialise hashMap[key]=[]
## design a suitable key
1. When the order of each element in the string/array doesn't matter, you can use the sorted string/array as the key.
![design key takeaway1](https://github.com/chopchap/leetcode/blob/main/images/designKey_takeaways1.png?raw=true)
2. If you only care about the offset of each value, usually the offset from the first value, you can use the offset as the key.
![design key takeaway2](https://github.com/chopchap/leetcode/blob/main/images/designKey_takeaways2.png?raw=true)
3. In a tree, you might want to directly use the TreeNode as key sometimes. But in most cases, the serialization of the subtree might be a better idea. (e.g. leetcode 652. Find Duplicate Subtrees)
![design key takeaway3](https://github.com/chopchap/leetcode/blob/main/images/designKey_takeaways3.png?raw=true)
4. In a matrix, you might want to use the row index or the column index as key.
5. In a Sudoku, you can combine the row index and the column index to identify which block this element belongs to.
![design key takeaway5](https://github.com/chopchap/leetcode/blob/main/images/designKey_takeaways5.png?raw=true)
6. Sometimes, in a matrix, you might want to aggregate the values in the same diagonal line. 
![design key takeaway6](https://github.com/chopchap/leetcode/blob/main/images/designKey_takeaways6.png?raw=true)
## n Sum problem
- if a + b + c == 0, we can always take advantage of the fact: a + b = -c with HashMap, therefore reduce the time complexity down to O(len(nums)^(n-1))
