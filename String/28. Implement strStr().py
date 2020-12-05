class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    """
    T=O(n), S=O(1), use Rabin Karp algo
    """
    L, n = len(needle), len(haystack)
    if L > n:
      return -1
    a = 26
    modulus = 2**31
    h_to_int = lambda i : ord(haystack[i]) - ord('a')
    needle_to_int = lambda i : ord(needle[i]) - ord('a')
    h = ref_h = 0
    for i in range(L):
      h = (h * a + h_to_int(i)) % modulus
      ref_h = (ref_h * a + needle_to_int(i)) % modulus
    if h == ref_h:
      return 0
    aL = pow(a, L, modulus) 
    for start in range(1, n - L + 1):
      h = (h * a - h_to_int(start - 1) * aL + h_to_int(start + L - 1)) % modulus
      if h == ref_h:
        return start
    return -1
