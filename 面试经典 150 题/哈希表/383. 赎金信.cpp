int cnt[26];

class Solution {
public:
  bool canConstruct(string ransomNote, string magazine) {
    if (ransomNote.size() > magazine.size()) return false;
    
    memset(cnt, 0, sizeof cnt);
    for (char c : magazine) cnt[c - 'a'] ++ ;

    for (char c : ransomNote)
      if (-- cnt[c - 'a'] < 0) return false;
    return true;
  }
};