// sliding window
// T=O(n)
// S=O(len(alphabet))

class Solution {
public:
  int lengthOfLongestSubstring(string s) {
    unordered_map<char, int> charLastIndex;
    int maxLen = 0;
    int windowLeft = 0;
    for (int i = 0; i < s.length(); i++) {
      if (charLastIndex.find(s[i]) != charLastIndex.end()) {
        int index = charLastIndex[s[i]];
        windowLeft = max(index+1, windowLeft);
      }
      maxLen = max(maxLen, i-windowLeft+1);
      charLastIndex[s[i]] = i;
    }
    return maxLen;
  }
};
