class Solution:
  def frequencySort(self, nums: List[int]) -> List[int]:
    d = collections.Counter(nums)
    pair = [(k, v) for k, v in d.items()]
    a = sorted(pair, key=lambda x: (x[1], -x[0]))
    ans = []
    for k, v in a:
      ans += [k]*v
    return ans
