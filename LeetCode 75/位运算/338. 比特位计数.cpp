class Solution {
public:
  vector<int> countBits(int n) {
    vector<int> res;

    for (int i = 0; i <= n; i ++ ) {
      int cnt = 0;
      for (int j = i; j; j -= j & -j) cnt ++ ;
      res.push_back(cnt);
    }
    
    return res;
  }
};