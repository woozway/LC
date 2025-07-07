class Solution {
public:
  vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
    int n1 = nums1.size(), n2 = nums2.size();
    auto &a = nums1, &b = nums2;

    unordered_set<int> S1, S2;
    for (auto x : a) S1.insert(x);
    for (auto x : b) S2.insert(x);

    vector<vector<int>> res(2);
    for (auto x : S1) if (!S2.count(x)) res[0].push_back(x);
    for (auto x : S2) if (!S1.count(x)) res[1].push_back(x);

    return res;
  }
};