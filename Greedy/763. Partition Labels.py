class Solution:
  def partitionLabels(self, S: str) -> List[int]:
    """
    record the farthest dist of char in S,
    init left&right to indicate a group, traverse S, 
    if dist[ch]>right, update right
    """
    dic = {}
    for i, ch in enumerate(S):
      dic[ch] = i
    left, right = 0, dic[S[0]]
    res = []
    for i, ch in enumerate(S):
      right = max(right, dic[ch])
      if i >= right:
        res.append(right - left + 1)
        left = right + 1 
    return res
