// hashing
// T=O(n)
// S=O(1)

class Solution {
public:
  char firstUniqChar(string s) {
    unordered_map<int, int> frequency;
    for (auto ch : s) {
      ++frequency[ch];
    }
    for (int i = 0; i < s.size(); ++i) {
      if (frequency[s[i]] == 1) {
        return s[i];
      }
    }
    return ' ';
  }
};
