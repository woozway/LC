class Solution:
  def numUniqueEmails(self, emails: List[str]) -> int:
    S = set()
    for e in emails:
      local, domain = e.split('@')
      if '+' in local:
        local = local[:local.index('+')]
      S.add(local.replace('.','') + '@' + domain)
    return len(S)
