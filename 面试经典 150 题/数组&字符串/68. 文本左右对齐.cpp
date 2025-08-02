class Solution {
  // join 返回用 sep 拼接 [i, j) 范围内的 words 组成的字符串
  string join(vector<string> &words, int l, int r, string sep) {
    string s = words[l];
    for (int i = l + 1; i < r; i ++ ) s += sep + words[i];
    return s;
  }

public:
  vector<string> fullJustify(vector<string>& words, int maxWidth) {
    int n = words.size();

    vector<string> res;
    for (int i = 0, j = 0; i < n; i = j) {
      int s = 0; // 统计这一行单词长度之和
      // 循环确定当前行可以放多少单词，注意单词之间应至少有一个空格
      while (j < n && s + words[j].size() + j - i <= maxWidth)
        s += words[j ++ ].size();

      if (j == n) { // 当前行是最后一行：单词左对齐，且单词之间应只有一个空格，在行末填充剩余空格
        string s = join(words, i, n, " ");
        res.push_back(s + string(maxWidth - s.size(), ' '));
        break;
      }

      int wordCnt = j - i;
      int spaceCnt = maxWidth - s;
      if (wordCnt == 1) { // 当前行只有一个单词：该单词左对齐，在行末填充剩余空格
        res.push_back(words[i] + string(spaceCnt, ' '));
        continue;
      }

      // 当前行不只一个单词
      int avgSpace = spaceCnt / (wordCnt - 1), extraSpace = spaceCnt % (wordCnt - 1);
      string s1 = join(words, i, i + extraSpace + 1, string(avgSpace + 1, ' '));
      string s2 = join(words, i + extraSpace + 1, j, string(avgSpace, ' '));
      res.push_back(s1 + string(avgSpace, ' ') + s2);
    }
    return res;
  }
};