// sliding window, max heap
// T=O(nlgn)
// S=O(n)

class Solution {
public:
  vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    if (nums.size() == 0) {
        return vector<int>();
    }
    int n = nums.size();
    priority_queue<pair<int, int>> q;
    for (int i = 0; i < k; ++i) {
      q.push({nums[i], i});
    }
    vector<int> ans = {q.top().first};
    for (int i = k; i < n; ++i) {
      q.push({nums[i], i});
      while (q.top().second <= i - k) {
        q.pop();
      }
      ans.push_back(q.top().first);
    }
    return ans;
  }
};
