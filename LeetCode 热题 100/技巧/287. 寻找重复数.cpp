class Solution {
public:
  int findDuplicate(vector<int>& nums) {
    int n = nums.size();
    auto &a = nums;

    // 数组版环形链表，同见：142. 环形链表 II
    int slow = 0, fast = 0;
    while (1) {
      fast = a[fast], fast = a[fast];
      slow = a[slow];
      if (slow == fast) break;
    }

    int res = 0;
    while (res != slow) {
      res = a[res];
      slow = a[slow];
    }
    return res;
  }
};