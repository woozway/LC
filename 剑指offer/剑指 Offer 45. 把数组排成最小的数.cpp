// sorting
// T=O(nlgn)
// S=O(n)

class Solution {
public:
  string minNumber(vector<int>& nums) {
    vector<string> v;
    for (auto& num : nums) {
      v.push_back(to_string(num));
    }
    sort(v.begin(), v.end(), [](string& a, string& b) {
      return a + b < b + a;
    });
    string ans;
    for (auto& s : v) {
      ans += s;
    }
    return ans;
  }
};
