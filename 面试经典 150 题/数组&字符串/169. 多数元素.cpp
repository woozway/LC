class Solution {
public:
  int majorityElement(vector<int>& nums) {
    int candidate = -1, cnt = 0;
    
    for (auto x : nums)
      if (x == candidate) cnt ++ ;
      else if (-- cnt < 0) {
        candidate = x;
        cnt = 1;
      }

    return candidate;
  }
};