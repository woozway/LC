class Solution {
public:
  void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    auto &a = nums1, &b = nums2;

    int i = m - 1, j = n - 1, k = m + n - 1;
    while (i >= 0 && j >= 0)
      if (a[i] >= b[j]) a[k -- ] = a[i -- ];
      else a[k -- ] = b[j -- ];

    while (i >= 0) a[k -- ] = a[i -- ];
    while (j >= 0) a[k -- ] = b[j -- ];
  }
};