const int N = 1e5 + 10;
int a[N], s1[N], s2[N];

class Solution {
public:
  vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    for (int i = 1; i <= n; i ++ ) a[i] = nums[i - 1];
    
    s1[0] = s1[n + 1] = 1;
    for (int i = 1; i <= n; i ++ ) s1[i] = s1[i - 1] * a[i];

    s2[0] = s2[n + 1] = 1;
    for (int i = n; i; i -- ) s2[i] = s2[i + 1] * a[i];

    vector<int> res;
    for (int i = 1; i <= n; i ++ ) res.push_back(s1[i - 1] * s2[i + 1]);
    return res;
  }
};