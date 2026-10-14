class Solution(object):

  def checkInclusion(self, s1, s2):
    if len(s1) > len(s2):
      return False

    mp = {}
    for i in s1:
      mp[i] = mp.get(i, 0) + 1

    left = 0
    count = len(s1)

    for r in range(len(s2)):
      ch = s2[r]
      if ch in mp:
        if mp[ch] > 0:
          count -= 1
        mp[ch] -= 1

      if r - left + 1 == len(s1):
        if count == 0:
          return True
        lch = s2[left]
        if lch in mp:
          if mp[lch] >= 0:
            count += 1
          mp[lch] += 1
        left += 1

    return False
