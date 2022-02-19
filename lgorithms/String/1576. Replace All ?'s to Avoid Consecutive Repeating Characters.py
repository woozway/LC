class Solution:
  def modifyString(self, s: str) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ret = list('0' + s + '0')
    for i in range(1, len(ret)-1):
      if ret[i] == '?':
        for j in range(26):
          if alphabet[j] not in {ret[i-1], ret[i+1]}:
            ret[i] = alphabet[j]
            break
    return ''.join(ret[1:-1])
